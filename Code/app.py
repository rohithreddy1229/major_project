from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import pickle
import numpy as np
import mysql.connector
from datetime import datetime, timedelta
import os
import cv2
import numpy as np
import tensorflow as tf
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Load pre-trained disease detection model
cnn = tf.keras.models.load_model('trained_plant_disease_model.h5')
class_names = ['Apple___apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy',
                'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 
                'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 
                'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 
                'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 
                'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 
                'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 
                'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 
                'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 
                'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 
                'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']  # Define your class names here

# Load crop recommendation model
model = pickle.load(open('model.pkl', 'rb'))

# Function to connect to MySQL database and fetch mean temperature, humidity, and moisture readings over the last 7 days
def fetch_mean_sensor_data():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='sampledata',
                                             user='root',
                                             password='')
        if connection.is_connected():
            cursor = connection.cursor()
            # Calculate start date for fetching data (7 days ago from current date)
            start_date = datetime.now() - timedelta(days=7)
            # Format start date as string
            start_date_str = start_date.strftime('%Y-%m-%d')
            # Fetch mean temperature, humidity, and moisture readings over the last 7 days
            query = f"SELECT AVG(temperature), AVG(humidity), AVG(moisture) FROM sampledata1 WHERE timestamp >= '{start_date_str}'"
            cursor.execute(query)
            row = cursor.fetchone()
            if row:
                temperature, humidity, moisture = row
                return temperature, humidity, moisture
            else:
                return None, None, None
    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to preprocess input and make crop recommendation
def recommend_crop(N, P, K, temperature, humidity, ph, rainfall):
    # Preprocess input
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    # Make prediction
    prediction = model.predict(features)

    # Convert prediction to scalar value
    predicted_crop = prediction[0] + 1

    # Map prediction to crop name
    crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

    if predicted_crop in crop_dict:
        crop = crop_dict[predicted_crop]
        return crop, f"{predicted_crop}.jpg"
    else:
        return "Sorry, unable to recommend a proper crop for this environment"

# Function to predict disease
def predict_disease(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (128,128))
    input_arr = np.array([image])
    predictions = cnn.predict(input_arr)
    result_index = np.argmax(predictions)
    return class_names[result_index]

from disease_details import get_additional_text_for_disease

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/crop_recommendation')
def crop_recommendation():
    # Fetch mean temperature, humidity, and moisture readings over the last 7 days from the database
    temperature, humidity, moisture = fetch_mean_sensor_data()
    # Calculate moisture percentage
    if moisture is not None:
        moisture_percentage = 100 - ((moisture / 1024) * 100)  # Assuming 0 is wet and 1024 is dry
    else:
        moisture_percentage = None
    return render_template('index.html', temperature=temperature, humidity=humidity, moisture_percentage=moisture_percentage)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        recommended_crop, crop_image = recommend_crop(N, P, K, temperature, humidity, ph, rainfall)
        return render_template('result.html', crop=recommended_crop, crop_image=crop_image)

@app.route('/disease_detection', methods=['GET', 'POST'])
def disease_detection():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            # Detect disease
            disease = predict_disease(file_path)
            # Additional text based on the detected disease
            additional_text = get_additional_text_for_disease(disease)
            return redirect(url_for('detected_disease', filename=filename, disease=disease, additional_text=additional_text))
    return render_template('upload.html')

@app.route('/detected_disease', methods=['GET', 'POST'])
def detected_disease():
    filename = request.args.get('filename')
    disease = request.args.get('disease')
    additional_text = request.args.get('additional_text')  # Ensure additional_text is retrieved from request
    if filename:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        return render_template('detected_disease.html', image_name=filename, disease=disease, additional_text=additional_text)
    # Redirect to the disease detection page if filename is not provided
    return redirect(url_for('disease_detection'))


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)