# disease_texts.py

def get_additional_text_for_disease(disease):
    disease_to_text = {

        'Apple___apple_scab': """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Apple Scab</u>.</h2>
        <p><strong>Apple Scab</strong> is a common and widespread fungal disease that primarily affects apple trees, though it can also infect pear trees to a lesser extent. It is prevalent in temperate regions worldwide and can lead to significant economic losses in apple orchards.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The primary symptoms of apple scab appear as olive-green to black lesions on leaves, fruit, and occasionally on young twigs. These lesions often have a velvety or scaly appearance. Infected leaves may become distorted or drop prematurely, reducing the tree's ability to photosynthesize effectively. On fruit, scab lesions can cause surface cracking and deformities, rendering them unmarketable.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Cultural Practices:</strong> Proper orchard management techniques, such as pruning to improve air circulation, maintaining proper tree spacing, and removing infected plant material, can help reduce the spread of apple scab.<br><br>
        <strong>Fungicide Application:</strong> Regular application of fungicides during the growing season can help prevent apple scab infection. Fungicides containing active ingredients such as mancozeb, captan, or sulfur are commonly used for control.<br><br>
        <strong>Resistant Varieties:</strong> Planting apple tree varieties that are resistant to apple scab can be an effective long-term strategy for managing the disease.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Apple scab is caused by the fungus Venturia inaequalis. The fungus overwinters in infected leaves and fruit on the ground, producing spores (ascospores) in the spring. These spores are then carried by wind or rain to infect newly emerging leaves and fruit. The disease thrives in cool, wet conditions, with optimal temperatures for infection ranging from 60°F to 75°F (15°C to 24°C), and it requires moisture on the leaf surface for spore germination and infection.</p>
        """
        ,


        'Apple___Black_rot': """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Apple Black Rot</u>.</h2>
        <p><strong>Apple black rot</strong> is a serious fungal disease that primarily affects apple trees but can also infect pear and other pome fruit trees. It is prevalent in regions with warm, humid climates and can cause significant losses in fruit production and quality.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of apple black rot typically appear on fruit, although leaves and shoots can also be affected. Initially, small, brown to black lesions develop on the fruit, often near the stem or calyx end. These lesions gradually expand and become sunken, with a wrinkled or leathery appearance. As the disease progresses, the entire fruit may become mummified, shriveled, and covered with black fungal spores (conidia). On leaves and shoots, black rot can cause brown lesions and dieback.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Sanitation: </strong>Remove and destroy any infected fruit, leaves, or branches to reduce the spread of the disease.<br><br>
        <strong>Pruning: </strong>Prune trees to improve air circulation and sunlight penetration, which can help reduce humidity and create less favorable conditions for fungal growth.<br><br>
        <strong>Fungicide Application: </strong>Apply fungicides preventatively during the growing season, especially during periods of warm, wet weather when the disease is most active. Fungicides containing active ingredients such as captan, thiophanate-methyl, or mancozeb are commonly used for control.<br><br>
        <strong>Fruit Bagging: </strong>Bagging fruit can provide a physical barrier against infection by preventing contact with fungal spores.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Apple black rot is caused by the fungus Botryosphaeria obtusa. The fungus overwinters in infected fruit mummies, dead branches, and cankers on the tree. In spring, fungal spores (conidia) are produced on these overwintering structures and are spread by wind, rain, or insects to infect newly developing fruit and leaves. Warm, humid conditions favor disease development, with optimal temperatures for infection ranging from 75°F to 85°F (24°C to 29°C). Rain or overhead irrigation provides the moisture necessary for spore germination and infection.</p>

        """
        
        ,


        'Apple___Cedar_apple_rust': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Apple Cedar Rust</u>.</h2>
        <p><Strong>Apple cedar rust</Strong> primarily affects apple and crabapple trees, as well as various species of juniper and cedar trees. It is a common fungal disease in regions where these host trees are present, causing significant damage to fruit crops and ornamental trees.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of apple cedar rust typically appear on leaves, fruit, and sometimes on twigs of apple and crabapple trees. Early symptoms include small yellow-orange spots on the upper surfaces of leaves, which gradually enlarge and develop a bright orange-red color as the disease progresses. These spots may also appear on fruit, causing deformities and reducing fruit quality. On juniper and cedar trees, apple cedar rust forms galls or swellings on the branches, which release spores during wet weather conditions.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Pruning: </strong>Remove and destroy any galls or infected branches on juniper and cedar trees to reduce the spread of the disease.<br><br>
        <strong>Sanitation: </strong>Remove and destroy any infected leaves, fruit, or branches from apple and crabapple trees to reduce the source of fungal spores.<br><br>
        <strong>Fungicide Application: </strong>Apply fungicides preventatively during the growing season, especially during periods of wet weather when spore production and infection are most likely to occur. Fungicides containing active ingredients such as myclobutanil or mancozeb are commonly used for control.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Apple cedar rust requires two host plants to complete its life cycle: apple or crabapple trees (genus Malus) and various species of juniper or cedar trees (genus Juniperus). The fungal pathogen overwinters as galls on juniper and cedar trees, where it produces spores (teliospores) in the spring. These spores are then carried by wind or rain to infect apple and crabapple trees, where they cause the characteristic orange-red lesions on leaves and fruit. Secondary spores (basidiospores) produced on apple and crabapple trees can then re-infect juniper and cedar trees, completing the disease cycle.</p>
        """
        ,

        'Apple___healthy': """<h2 style="font-weight: bold; font-size: 26px; text-align: center;">Your crop is healthy🥳</h2>""",


        'Blueberry___healthy': """<h2 style="font-weight: bold; font-size: 26px; text-align: center;">Your crop is healthy🥳</h2>""",


        'Cherry_(including_sour)___Powdery_mildew': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Cherry Powdery Mildew</u>.</h2>
        <p><Strong>Cherry powdery mildew </Strong>primarily affects cherry trees, including sweet cherry (Prunus avium) and sour cherry (Prunus cerasus) varieties. It is a common fungal disease in regions with temperate climates, causing significant damage to foliage and reducing fruit yield and quality.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of cherry powdery mildew typically appear as a white to grayish powdery fungal growth on the surfaces of leaves, shoots, flowers, and fruit. This powdery coating consists of fungal spores and mycelium. Infected leaves may become distorted, curl upwards, and eventually drop prematurely. Severe infections can lead to defoliation, weakening the tree and reducing its ability to produce fruit.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Cultural Practices: </strong>Practices such as proper spacing of trees, pruning to improve air circulation, and removal of infected plant debris can help reduce the spread of cherry powdery mildew.<br><br>
        <strong>Fungicide Application: </strong>Apply fungicides preventatively during the growing season, especially during periods of warm, dry weather when powdery mildew is most active. Fungicides containing active ingredients such as sulfur, potassium bicarbonate, or synthetic fungicides like myclobutanil are commonly used for control.<br><br>
        <strong>Resistant Varieties: </strong>Planting cherry tree varieties that are resistant to powdery mildew can help reduce the risk of infection.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Cherry powdery mildew is caused by the fungus Podosphaera clandestina. The fungus overwinters as dormant structures (cleistothecia) on infected cherry tree debris. In spring, when conditions are favorable (moderate temperatures and high humidity), the fungus produces airborne spores (conidia) that are carried by wind to infect new cherry foliage and fruit. Unlike some other fungal diseases, cherry powdery mildew thrives in warm, dry weather conditions, with optimal temperatures for infection ranging from 68°F to 77°F (20°C to 25°C).</p>
        """
        ,
        'Cherry_(including_sour)___healthy': """<h2 style="font-weight: bold; font-size: 26px; text-align: center;">Your crop is healthy🥳</h2>""",
        
        
        'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Corn(Maize) Cercospora leaf spot and Gray leaf spot</u>.</h2>
        <p>In Corn (Maize) <Strong>cercospora leaf spot</strong> and <strong>gray leaf spot</Strong> are two distinct fungal diseases that affect maize (corn) plants.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>Symptoms include small, dark brown to black spots with a yellow halo on maize leaves. These spots may merge, leading to large necrotic areas, which can result in premature leaf death.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Crop rotation: </strong>Avoid planting maize in the same field continuously.<br><br>
        <strong>Tillage: </strong>Deep tillage can help bury infected crop residues, reducing the source of inoculum.<br><br>
        <strong>Resistant varieties: </strong>Plant maize hybrids that are resistant or tolerant to Cercospora leaf spot.</p>
        <strong>Fungicide application: </strong>Fungicides containing active ingredients such as strobilurins or triazoles can be applied preventatively to control the disease.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Cercospora leaf spot is caused by the fungus Cercospora zeae-maydis.</p>
        <p>Gray leaf spot is caused by the fungus Cercospora zeae-maydis (same as cercospora leaf spot) or Cercospora zeina.</p>


        """
        ,
        'Corn_(maize)___Common_rust_': 

        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Corn Common Rust</u>.</h2>
        <p><strong>Corn Common Rust</strong> is a fungal disease caused by the pathogen <i>Puccinia sorghi</i> that affects corn (maize) plants. It is a widespread disease in regions where corn is cultivated, particularly in temperate and tropical climates.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The characteristic symptoms of corn common rust include small, round to elongated, reddish-brown to black pustules or lesions on the leaves, stalks, and husks of corn plants. These pustules may appear powdery and can coalesce, covering large areas of the plant tissue. Severe infections can lead to stunted growth, reduced photosynthesis, and decreased yield.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Resistant Varieties:</strong> Planting corn cultivars that have genetic resistance to common rust can help mitigate the impact of the disease. Many modern corn hybrids have been bred for resistance to this fungal pathogen.<br><br>
        <strong>Crop Rotation:</strong> Practicing crop rotation can disrupt the life cycle of the fungus and reduce the build-up of inoculum in the soil, decreasing the risk of infection in subsequent corn crops.<br><br>
        <strong>Fungicide Application:</strong> In severe cases or when susceptible varieties are planted, fungicides can be applied preventively to protect corn plants from common rust infection. Fungicides containing active ingredients such as triazoles, strobilurins, or azoles are commonly used for control.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Corn common rust is caused by the fungus <i>Puccinia sorghi</i>. The disease spreads through airborne spores, which are produced in abundance within the pustules on infected plants. These spores can be carried by wind currents over long distances, facilitating the spread of the disease within and between fields. Optimal conditions for common rust development include moderate temperatures ranging from 60°F to 80°F (15°C to 27°C) and high humidity levels.</p>
        """
        ,
        
        'Corn_(maize)___Northern_Leaf_Blight': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Corn Northern Leaf Blight</u>.</h2>
        <p><strong>Corn Northern Leaf Blight</strong>, caused by the fungus <i>Exserohilum turcicum</i>, is a devastating foliar disease of corn (maize) plants. It is particularly prevalent in regions with humid and warm climates, posing a significant threat to corn production.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of corn northern leaf blight typically appear as long, elliptical lesions on the leaves of corn plants. These lesions may start as small, water-soaked spots and gradually enlarge, turning tan to brown in color with irregular margins. Severe infections can lead to widespread blighting of the leaves, reducing photosynthetic capacity and ultimately impacting yield.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Resistant Varieties:</strong> Planting corn hybrids with genetic resistance to northern leaf blight is an effective strategy for managing the disease. Many commercial corn varieties offer varying levels of resistance to this fungal pathogen.<br><br>
        <strong>Crop Rotation:</strong> Rotating crops with non-host species can help reduce the build-up of inoculum in the soil and lower the risk of northern leaf blight infection in subsequent corn crops.<br><br>
        <strong>Fungicide Application:</strong> When environmental conditions favor disease development or when susceptible varieties are planted, fungicides can be applied preventively to protect corn plants from northern leaf blight. Fungicides containing active ingredients such as azoxystrobin, propiconazole, or chlorothalonil are commonly used for control.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Corn northern leaf blight is caused by the fungus <i>Exserohilum turcicum</i>. The disease spreads through airborne spores, which are produced in abundance on infected corn debris and spread by wind or rain splash. Optimal conditions for disease development include moderate temperatures ranging from 68°F to 77°F (20°C to 25°C) and extended periods of leaf wetness or high humidity.</p>
        """
        
        ,
        'Corn_(maize)___healthy': """<h2 style="font-weight: bold; font-size: 26px; text-align: center;">Your crop is healthy🥳</h2>""",
        
        'Grape___Black_rot': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Grape Black Rot</u>.</h2>
        <p><strong>Grape Black Rot</strong>, caused by the fungus <i>Guignardia bidwellii</i>, is a destructive disease affecting grapevines, particularly in regions with warm, humid climates. It can lead to significant economic losses in vineyards by reducing yield and quality of grapes.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of grape black rot first appear as small, water-soaked spots on leaves, which gradually enlarge and turn brown or black. These lesions may become necrotic and cause defoliation, weakening the vine. On fruit, black rot manifests as circular, sunken lesions that start green and then turn brown to black as they expand. Infected grapes often shrivel and become mummified on the vine.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Cultural Practices:</strong> Good vineyard management practices, such as proper pruning to improve air circulation, removal of infected plant material, and canopy management to reduce humidity around the grape clusters, can help minimize the spread of black rot.<br><br>
        <strong>Fungicide Application:</strong> Regular application of fungicides, especially during periods of high disease pressure, can effectively control black rot. Fungicides containing active ingredients such as captan, mancozeb, or myclobutanil are commonly used for management.<br><br>
        <strong>Fruit Mummification Removal:</strong> Prompt removal and destruction of mummified fruit from the vine and surrounding areas can reduce inoculum and prevent future infections.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Grape black rot is caused by the fungus <i>Guignardia bidwellii</i>. The fungus overwinters in infected plant debris, such as fallen leaves and mummified fruit, and produces spores (conidia) in the spring. These spores are spread by rain, wind, or insects and can infect new growth and fruit during wet conditions. Optimal temperatures for disease development range from 77°F to 86°F (25°C to 30°C), with prolonged periods of leaf wetness or high humidity favoring infection.</p>
        """
        ,

        'Grape___Esca_(Black_Measles)': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Grape Esca (Black Measles)</u>.</h2>
        <p><strong>Grape Esca</strong>, also known as <strong>Black Measles</strong>, is a complex disease syndrome affecting grapevines worldwide. It is caused by a combination of fungi, including <i>Phaeoacremonium spp.</i>, <i>Phaeomoniella chlamydospora</i>, and others. Esca is a significant concern for grape growers due to its destructive nature and the difficulty in managing its spread.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>Grape esca exhibits a range of symptoms, including foliar, vascular, and wood symptoms. Foliar symptoms often include yellowing and browning of the leaves, as well as the appearance of dark streaks or spots. Vascular symptoms involve discoloration and necrosis of the vascular tissues, leading to wilting and dieback of shoots. Wood symptoms manifest as dark streaks or lesions in the wood, commonly referred to as "tiger stripes."</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Vineyard Sanitation:</strong> Removal and destruction of infected plant material, including pruning wood showing symptoms of esca, can help reduce inoculum and slow the spread of the disease within the vineyard.<br><br>
        <strong>Canopy Management:</strong> Proper canopy management practices, such as adequate pruning to improve air circulation and reduce humidity within the canopy, can help minimize the risk of esca infection.<br><br>
        <strong>Grafting:</strong> Some grapevine rootstocks are more resistant to esca than others. Grafting onto resistant rootstocks may help mitigate the impact of the disease in vineyards.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Grape esca is caused by a complex of fungi, including <i>Phaeoacremonium spp.</i>, <i>Phaeomoniella chlamydospora</i>, and others. These fungi typically enter the vine through pruning wounds or natural openings and establish themselves within the vascular tissues, where they spread systemically throughout the plant. Environmental stressors, such as drought or heat stress, can exacerbate esca symptoms. Optimal conditions for disease development include warm temperatures and periods of high humidity.</p>
        """
        
        ,


        'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Grape Leaf Blight (Isariopsis Leaf Spot)</u>.</h2>
        <p><strong>Grape Leaf Blight</strong>, also known as <strong>Isariopsis Leaf Spot</strong>, is a fungal disease caused by the pathogen <i>Isariopsis griseola</i>. It primarily affects grapevines, leading to leaf damage and potentially reducing yield and fruit quality.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of grape leaf blight typically appear as small, circular to irregularly shaped spots on the leaves. These spots may start as water-soaked lesions and gradually turn brown to grayish in color with a dark border. Severe infections can cause defoliation, weaken the vine, and impact fruit ripening.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Vineyard Sanitation:</strong> Removal and destruction of infected plant material, such as diseased leaves and debris, can help reduce inoculum and limit the spread of grape leaf blight within the vineyard.<br><br>
        <strong>Fungicide Application:</strong> Regular application of fungicides, especially during periods of high disease pressure, can help manage grape leaf blight. Fungicides containing active ingredients such as copper compounds, mancozeb, or chlorothalonil are commonly used for control.<br><br>
        <strong>Canopy Management:</strong> Proper canopy management practices, including pruning to improve air circulation and reduce humidity within the canopy, can help minimize the risk of grape leaf blight infection.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Grape leaf blight is caused by the fungus <i>Isariopsis griseola</i>. The disease spreads through spores produced on infected plant material, which can be disseminated by wind, rain splash, or through human activities such as pruning. Optimal conditions for disease development include warm temperatures ranging from 68°F to 86°F (20°C to 30°C) and extended periods of leaf wetness or high humidity.</p>
        """
        ,

        'Grape___healthy': """<h2 style="font-weight: bold; font-size: 26px; text-align: center;">Your crop is healthy🥳</h2>""",
        
        'Orange___Haunglongbing_(Citrus_greening)': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Orange Huanglongbing (Citrus Greening)</u>.</h2>
        <p><strong>Orange Huanglongbing</strong>, commonly known as <strong>Citrus Greening</strong>, is a devastating bacterial disease affecting citrus trees, including oranges. It is caused by the bacterium <i>Candidatus</i> Liberibacter spp. and is transmitted by the Asian citrus psyllid (<i>Diaphorina citri</i>). Citrus greening poses a severe threat to citrus production worldwide.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of citrus greening are diverse and include yellowing of leaves, often with asymmetrical blotchy mottling. Leaves may also exhibit a pattern of "green islands" where small patches of healthy tissue remain within the yellowed areas. Infected trees may produce small, lopsided, and bitter-tasting fruit with aborted seeds. Premature fruit drop and dieback of branches are common symptoms as the disease progresses.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Vector Control:</strong> Managing populations of the Asian citrus psyllid, the primary vector of citrus greening, is crucial for disease prevention. This can be achieved through insecticide applications, biological control methods, and cultural practices to reduce psyllid habitat.<br><br>
        <strong>Early Detection and Removal:</strong> Prompt detection of infected trees and removal of symptomatic plants can help prevent the spread of citrus greening within orchards. Quarantine measures may be implemented in affected areas to limit the movement of infected plant material.<br><br>
        <strong>Tree Nutrition and Care:</strong> Maintaining optimal tree health through proper nutrition, irrigation, and cultural practices can help citrus trees withstand the effects of greening and reduce their susceptibility to infection.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Citrus greening is caused by the bacterium <i>Candidatus</i> Liberibacter spp., which is transmitted by the Asian citrus psyllid (<i>Diaphorina citri</i>). Once infected, citrus trees typically remain asymptomatic for several months to years before exhibiting symptoms. The bacterium resides in the phloem tissues of the tree, disrupting nutrient transport and leading to the characteristic symptoms of greening. Optimal conditions for disease transmission include warm temperatures and the presence of infected psyllids.</p>
        """
        ,

        'Peach___Bacterial_spot': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Peach Bacterial Spot</u>.</h2>
        <p><strong>Peach Bacterial Spot</strong>, caused by the bacterium <i>Xanthomonas arboricola pv. pruni</i>, is a common and destructive disease affecting peach and other stone fruit trees. It can lead to significant economic losses in orchards, particularly in regions with warm and humid climates.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of peach bacterial spot typically appear as small, water-soaked lesions on leaves, fruit, and stems. These lesions may turn dark brown to black and develop a raised, rough texture as they enlarge. Infected leaves may exhibit angular necrotic spots with yellow halos, leading to premature defoliation and reduced tree vigor. On fruit, lesions can cause surface cracking and corky tissue, rendering them unmarketable.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Cultural Practices:</strong> Proper orchard sanitation, including removal of infected plant material, can help reduce inoculum and slow the spread of bacterial spot within the orchard. Pruning to improve air circulation and reduce humidity within the canopy can also aid in disease management.<br><br>
        <strong>Copper Sprays:</strong> Application of copper-based bactericides during the dormant season and throughout the growing season can help suppress bacterial populations and reduce disease severity.<br><br>
        <strong>Resistant Varieties:</strong> Planting peach cultivars with genetic resistance to bacterial spot can provide effective long-term control of the disease.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Peach bacterial spot is caused by the bacterium <i>Xanthomonas arboricola pv. pruni</i>. The bacterium can overwinter in infected plant debris and spread to new growth during periods of rain or overhead irrigation. Optimal conditions for disease development include warm temperatures ranging from 75°F to 85°F (24°C to 29°C) and high humidity. Bacterial spot can also be spread through mechanical means, such as pruning tools and equipment.</p>
        """
        ,

        'Peach___healthy': """<h2 style="font-weight: bold; font-size: 26px; text-align: center;">Your crop is healthy🥳</h2>""",
        
        'Pepper,_bell___Bacterial_spot': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Pepper Bell Bacterial Spot</u>.</h2>
        <p><strong>Pepper Bell Bacterial Spot</strong> is a bacterial disease caused by <i>Xanthomonas campestris</i> pv. <i>vesicatoria</i>, which affects pepper plants, including bell peppers. It is a significant concern for pepper growers, leading to reduced yield and fruit quality.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of pepper bell bacterial spot include small, water-soaked lesions on leaves, stems, and fruit. These lesions may turn dark brown to black and develop a raised, rough texture as they enlarge. Infected leaves may exhibit angular necrotic spots with yellow halos, leading to premature defoliation and reduced plant vigor. On fruit, lesions can cause surface blemishes and may lead to fruit drop.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Cultural Practices:</strong> Proper sanitation and management of crop residues can help reduce inoculum and slow the spread of bacterial spot within the pepper field. Crop rotation with non-host crops can also help break the disease cycle.<br><br>
        <strong>Pathogen-free Seed:</strong> Planting certified disease-free pepper seeds can help reduce the risk of introducing bacterial spot into the field.<br><br>
        <strong>Fungicide Application:</strong> Copper-based bactericides or other registered bactericides can be applied preventively to protect pepper plants from bacterial spot infection. Application timing and frequency should follow label instructions.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Pepper bell bacterial spot is caused by the bacterium <i>Xanthomonas campestris</i> pv. <i>vesicatoria</i>. The bacterium can survive in infected plant debris and spread to new plants through rain splash, wind-driven rain, or mechanical means. Optimal conditions for disease development include warm temperatures ranging from 75°F to 85°F (24°C to 29°C) and high humidity. Overhead irrigation or frequent rainfall can exacerbate disease spread.</p>
        """
        ,
        
        'Pepper,_bell___healthy': """<h2 style="font-weight: bold; font-size: 26px; text-align: center;">Your crop is healthy🥳</h2>""",
        
        'Potato___Early_blight': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Potato Early Blight</u>.</h2>
        <p><strong>Potato Early Blight</strong>, caused by the fungus <i>Alternaria solani</i>, is a common foliar disease affecting potato plants. It can lead to significant yield losses and reduced tuber quality if left unmanaged.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of potato early blight typically appear on the lower leaves of the plant and progress upward. Initial symptoms include small, dark brown spots or lesions on the leaves, which may develop concentric rings and yellow halos as they enlarge. Severe infections can cause leaf yellowing, premature defoliation, and a reduction in photosynthetic capacity.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Sanitation:</strong> Removal and destruction of infected plant material, including affected leaves and debris, can help reduce inoculum and slow the spread of early blight within the potato field.<br><br>
        <strong>Resistant Varieties:</strong> Planting potato cultivars with genetic resistance to early blight can provide effective control of the disease. Resistant varieties may exhibit fewer symptoms and require fewer fungicide applications.<br><br>
        <strong>Fungicide Application:</strong> Regular application of fungicides, particularly during periods of high disease pressure, can help manage early blight in potato crops. Fungicides containing active ingredients such as chlorothalonil, mancozeb, or azoxystrobin are commonly used for control.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Potato early blight is caused by the fungus <i>Alternaria solani</i>. The fungus overwinters in infected plant debris and soil, producing spores (conidia) that are spread by wind, rain splash, or mechanical means. Optimal conditions for disease development include warm temperatures ranging from 75°F to 85°F (24°C to 29°C) and extended periods of leaf wetness or high humidity.</p>
        """
        ,
        
        'Potato___Late_blight': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Potato Late Blight</u>.</h2>
        <p><strong>Potato Late Blight</strong>, caused by the oomycete pathogen <i>Phytophthora infestans</i>, is one of the most destructive diseases affecting potato plants worldwide. It was historically responsible for devastating famines, such as the Irish Potato Famine in the 19th century, and continues to pose a significant threat to potato production.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of potato late blight typically appear as water-soaked lesions on leaves, which rapidly expand and turn brown to black in color. These lesions may exhibit a fuzzy or moldy appearance under humid conditions. Infected foliage may become necrotic and undergo rapid defoliation. Tubers can also be infected, leading to dark, firm lesions that can rot in storage.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Resistant Varieties:</strong> Planting potato cultivars with genetic resistance to late blight can provide effective control of the disease. Resistant varieties may exhibit fewer symptoms and require fewer fungicide applications.<br><br>
        <strong>Fungicide Application:</strong> Regular application of fungicides is essential for managing late blight in potato crops, especially during periods of high disease pressure. Fungicides containing active ingredients such as chlorothalonil, mancozeb, or metalaxyl are commonly used for control.<br><br>
        <strong>Cultural Practices:</strong> Good crop rotation practices, removal and destruction of infected plant material, and proper irrigation management can help reduce the risk of late blight outbreaks in potato fields.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Potato late blight is caused by the oomycete pathogen <i>Phytophthora infestans</i>. The pathogen thrives in cool, humid conditions and can spread rapidly during periods of wet weather. Spores are produced on infected foliage and can be disseminated by wind, rain splash, or irrigation water. Optimal temperatures for disease development range from 60°F to 75°F (15°C to 24°C), with leaf wetness periods of at least 6-8 hours.</p>
        """
        ,
        
        'Potato___healthy': """<h2 style="font-weight: bold; font-size: 26px; text-align: center;">Your crop is healthy🥳</h2>""",
        
        'Raspberry___healthy': """<h2 style="font-weight: bold; font-size: 26px; text-align: center;">Your crop is healthy🥳</h2>""",
        
        'Soybean___healthy': """<h2 style="font-weight: bold; font-size: 26px; text-align: center;">Your crop is healthy🥳</h2>""",
        
        'Squash___Powdery_mildew': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Squash Powdery Mildew</u>.</h2>
        <p><strong>Squash Powdery Mildew</strong> is a fungal disease caused by various species of the genus <i>Podosphaera</i>. It commonly affects squash plants, including zucchini, pumpkins, and other cucurbits, particularly in warm and humid climates.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of squash powdery mildew typically appear as white to grayish powdery patches on the leaves, stems, and sometimes the fruit of affected plants. These patches may coalesce to cover large areas of the plant tissue, causing leaf distortion and reduced photosynthetic activity. Severe infections can lead to premature defoliation and reduced yield.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Cultural Practices:</strong> Proper spacing between plants, adequate air circulation, and avoiding overhead irrigation can help reduce humidity levels and minimize the spread of powdery mildew in squash crops. Additionally, removing and destroying infected plant material can help prevent further disease development.<br><br>
        <strong>Fungicide Application:</strong> Regular application of fungicides, particularly those containing active ingredients such as sulfur, potassium bicarbonate, or neem oil, can help manage powdery mildew in squash plants. Application timing and frequency should follow label instructions and be based on disease pressure and environmental conditions.<br><br>
        <strong>Resistant Varieties:</strong> Planting squash varieties with genetic resistance to powdery mildew can provide effective long-term control of the disease.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Squash powdery mildew is caused by various species of the genus <i>Podosphaera</i>. The fungus thrives in warm temperatures and high humidity, with optimal conditions for disease development occurring between 60°F to 80°F (15°C to 27°C). Spores are produced on infected plant tissue and can be dispersed by wind to infect new plants. Overcrowded plantings and dense foliage can exacerbate disease spread by creating favorable conditions for fungal growth.</p>
        """
        ,
        
        'Strawberry___Leaf_scorch': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Strawberry Leaf Scorch</u>.</h2>
        <p><strong>Strawberry Leaf Scorch</strong>, caused by the bacterium <i>Xanthomonas fragariae</i>, is a bacterial disease that affects strawberry plants. It can lead to reduced yield and quality of strawberries, particularly in warm and humid growing conditions.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of strawberry leaf scorch typically appear as small, water-soaked lesions on the leaves, which may gradually enlarge and turn brown to black in color. These lesions may exhibit angular shapes and can coalesce to cover large areas of the leaf surface. Infected leaves may become necrotic and undergo premature defoliation, leading to reduced photosynthetic capacity and stunted growth.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Cultural Practices:</strong> Proper spacing between strawberry plants, adequate air circulation, and avoiding overhead irrigation can help reduce humidity levels and minimize the spread of leaf scorch. Removing and destroying infected plant material, including affected leaves and runners, can also help prevent further disease development.<br><br>
        <strong>Fungicide Application:</strong> Regular application of copper-based bactericides or other registered bactericides can help manage leaf scorch in strawberry crops. Application timing and frequency should follow label instructions and be based on disease pressure and environmental conditions.<br><br>
        <strong>Resistant Varieties:</strong> Planting strawberry cultivars with genetic resistance to leaf scorch can provide effective long-term control of the disease.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Strawberry leaf scorch is caused by the bacterium <i>Xanthomonas fragariae</i>. The bacterium thrives in warm temperatures and high humidity, with optimal conditions for disease development occurring between 60°F to 80°F (15°C to 27°C). It can spread through infected plant material, splashing water, and contaminated tools or equipment. Overcrowded plantings and dense foliage can exacerbate disease spread by creating favorable conditions for bacterial growth.</p>
        """
        ,
        
        'Strawberry___healthy': """<h2 style="font-weight: bold; font-size: 26px; text-align: center;">Your crop is healthy🥳</h2>""",
        
        'Tomato___Bacterial_spot': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Tomato Bacterial Spot</u>.</h2>
        <p><strong>Tomato Bacterial Spot</strong> is a bacterial disease caused by <i>Xanthomonas vesicatoria</i>, affecting tomato plants. It can lead to significant yield losses and reduced fruit quality if left unmanaged.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of tomato bacterial spot typically appear as small, water-soaked lesions on the leaves, which may develop into dark, necrotic spots with a yellow halo. These spots may coalesce to form large lesions, leading to leaf yellowing, wilting, and premature defoliation. On fruit, bacterial spot lesions are typically small, dark, and sunken, often surrounded by a yellow halo.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Cultural Practices:</strong> Proper sanitation, including removal and destruction of infected plant material, can help reduce inoculum and slow the spread of bacterial spot within the tomato field. Crop rotation with non-host crops can also help break the disease cycle.<br><br>
        <strong>Resistant Varieties:</strong> Planting tomato cultivars with genetic resistance to bacterial spot can provide effective control of the disease. Resistant varieties may exhibit fewer symptoms and require fewer fungicide applications.<br><br>
        <strong>Fungicide Application:</strong> Copper-based bactericides or other registered bactericides can be applied preventively to protect tomato plants from bacterial spot infection. Application timing and frequency should follow label instructions and be based on disease pressure and environmental conditions.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Tomato bacterial spot is caused by the bacterium <i>Xanthomonas vesicatoria</i>. The bacterium can survive in infected plant debris and soil, spreading to new plants through rain splash, wind-driven rain, or mechanical means. Optimal conditions for disease development include warm temperatures ranging from 75°F to 85°F (24°C to 29°C) and high humidity. Overhead irrigation or frequent rainfall can exacerbate disease spread.</p>
        """
        ,
        
        'Tomato___Early_blight': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Tomato Early Blight</u>.</h2>
        <p><strong>Tomato Early Blight</strong>, caused by the fungus <i>Alternaria solani</i>, is a common foliar disease affecting tomato plants. It can lead to significant yield losses and reduced fruit quality if left unmanaged.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of tomato early blight typically appear as small, dark brown lesions on the lower leaves of the plant, which may have concentric rings and yellow halos. As the disease progresses, the lesions may enlarge and coalesce, leading to defoliation and reduced plant vigor. Fruit may also become infected, developing dark, sunken lesions with concentric rings.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Cultural Practices:</strong> Proper sanitation, including removal and destruction of infected plant material, can help reduce inoculum and slow the spread of early blight within the tomato field. Crop rotation with non-host crops can also help break the disease cycle.<br><br>
        <strong>Resistant Varieties:</strong> Planting tomato cultivars with genetic resistance to early blight can provide effective control of the disease. Resistant varieties may exhibit fewer symptoms and require fewer fungicide applications.<br><br>
        <strong>Fungicide Application:</strong> Regular application of fungicides, particularly those containing active ingredients such as chlorothalonil or mancozeb, can help manage early blight in tomato crops. Application timing and frequency should follow label instructions and be based on disease pressure and environmental conditions.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Tomato early blight is caused by the fungus <i>Alternaria solani</i>. The fungus can overwinter in infected plant debris and soil, spreading to new plants through wind-driven rain, splashing water, or mechanical means. Optimal conditions for disease development include warm temperatures ranging from 75°F to 85°F (24°C to 29°C) and high humidity. Overhead irrigation or frequent rainfall can exacerbate disease spread.</p>
        """
        ,
        
        'Tomato___Late_blight': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Tomato Late Blight</u>.</h2>
        <p><strong>Tomato Late Blight</strong>, caused by the oomycete pathogen <i>Phytophthora infestans</i>, is one of the most destructive diseases affecting tomato plants. It can lead to significant yield losses and reduced fruit quality if left unmanaged.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of tomato late blight typically appear as water-soaked lesions on the leaves, which rapidly expand and turn brown to black in color. These lesions may have a fuzzy or moldy appearance under humid conditions. Infected foliage may become necrotic and undergo rapid defoliation. Fruit can also be infected, developing dark, sunken lesions with a firm, granular texture.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Resistant Varieties:</strong> Planting tomato cultivars with genetic resistance to late blight can provide effective control of the disease. Resistant varieties may exhibit fewer symptoms and require fewer fungicide applications.<br><br>
        <strong>Fungicide Application:</strong> Regular application of fungicides is essential for managing late blight in tomato crops, especially during periods of high disease pressure. Fungicides containing active ingredients such as chlorothalonil, mancozeb, or metalaxyl are commonly used for control. Application timing and frequency should follow label instructions and be based on disease pressure and environmental conditions.<br><br>
        <strong>Cultural Practices:</strong> Good crop rotation practices, removal and destruction of infected plant material, and proper irrigation management can help reduce the risk of late blight outbreaks in tomato fields.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Tomato late blight is caused by the oomycete pathogen <i>Phytophthora infestans</i>. The pathogen thrives in cool, humid conditions and can spread rapidly during periods of wet weather. Spores are produced on infected foliage and can be dispersed by wind, rain splash, or irrigation water. Optimal temperatures for disease development range from 60°F to 75°F (15°C to 24°C), with leaf wetness periods of at least 6-8 hours.</p>
        """
        ,
        
        'Tomato___Leaf_Mold': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Tomato Leaf Mold</u>.</h2>
        <p><strong>Tomato Leaf Mold</strong>, caused by the fungus <i>Fulvia fulva</i> (formerly known as <i>Cladosporium fulvum</i>), is a common fungal disease affecting tomato plants. It can lead to significant yield losses and reduced fruit quality if left unmanaged, particularly in warm and humid growing conditions.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of tomato leaf mold typically appear as yellowish-green or pale yellow spots on the upper surface of the leaves. These spots may gradually enlarge and develop into fuzzy, grayish-white patches on the underside of the leaves, giving them a moldy appearance. Infected leaves may become distorted and curl upward, and severe infections can lead to defoliation and reduced plant vigor.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Cultural Practices:</strong> Proper spacing between tomato plants, adequate air circulation, and avoiding overhead irrigation can help reduce humidity levels and minimize the spread of leaf mold within the tomato field. Removing and destroying infected plant material, including affected leaves and debris, can also help prevent further disease development.<br><br>
        <strong>Fungicide Application:</strong> Regular application of fungicides, particularly those containing active ingredients such as chlorothalonil or mancozeb, can help manage leaf mold in tomato crops. Application timing and frequency should follow label instructions and be based on disease pressure and environmental conditions.<br><br>
        <strong>Resistant Varieties:</strong> Planting tomato cultivars with genetic resistance to leaf mold can provide effective control of the disease. Resistant varieties may exhibit fewer symptoms and require fewer fungicide applications.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Tomato leaf mold is caused by the fungus <i>Fulvia fulva</i>. The fungus thrives in warm temperatures and high humidity, with optimal conditions for disease development occurring between 70°F to 80°F (21°C to 27°C). Spores are produced on infected plant tissue and can be disseminated by wind, water splash, or through human activities. Overhead irrigation or frequent rainfall can exacerbate disease spread.</p>
        """
        ,
        
        'Tomato___Septoria_leaf_spot': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Tomato Septoria Leaf Spot</u>.</h2>
        <p><strong>Tomato Septoria Leaf Spot</strong>, caused by the fungus <i>Septoria lycopersici</i>, is a common foliar disease affecting tomato plants. It can lead to significant yield losses and reduced fruit quality if left unmanaged.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of tomato septoria leaf spot typically appear as small, circular lesions with dark brown centers and lighter-colored margins on the lower leaves of the plant. As the disease progresses, the lesions may increase in size and number, eventually causing leaf yellowing, wilting, and premature defoliation. Fruit can also become infected, developing dark, sunken lesions.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Cultural Practices:</strong> Proper sanitation, including removal and destruction of infected plant material, can help reduce inoculum and slow the spread of septoria leaf spot within the tomato field. Crop rotation with non-host crops can also help break the disease cycle.<br><br>
        <strong>Resistant Varieties:</strong> Planting tomato cultivars with genetic resistance to septoria leaf spot can provide effective control of the disease. Resistant varieties may exhibit fewer symptoms and require fewer fungicide applications.<br><br>
        <strong>Fungicide Application:</strong> Regular application of fungicides, particularly those containing active ingredients such as chlorothalonil or mancozeb, can help manage septoria leaf spot in tomato crops. Application timing and frequency should follow label instructions and be based on disease pressure and environmental conditions.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Tomato septoria leaf spot is caused by the fungus <i>Septoria lycopersici</i>. The fungus can survive in infected plant debris and soil, spreading to new plants through rain splash, wind-driven rain, or mechanical means. Optimal conditions for disease development include warm temperatures ranging from 65°F to 80°F (18°C to 27°C) and high humidity. Overhead irrigation or frequent rainfall can exacerbate disease spread.</p>
        """
        ,
        
        'Tomato___Spider_mites Two-spotted_spider_mite': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected pest is <u>Tomato Spider Mites</u>.</h2>
        <p><strong>Tomato Spider Mites</strong>, including the Two-Spotted Spider Mite (<i>Tetranychus urticae</i>), are common pests that can cause significant damage to tomato plants by feeding on plant tissues and sucking out cell contents. Two-spotted spider mites are particularly notorious for their ability to rapidly reproduce under warm and dry conditions, leading to widespread infestations.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of tomato spider mite infestation typically include stippling or yellowing of leaves caused by mite feeding, which can progress to bronzing, browning, or necrosis under severe infestations. Fine webbing may also be visible on the undersides of leaves, particularly in heavily infested areas. In severe cases, leaves may become distorted, curled, or drop prematurely, and fruit production can be reduced.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Management</h2>
        <p><strong>Cultural Practices:</strong> Maintaining proper plant hygiene by removing weeds and debris, and regular pruning to improve air circulation, can help reduce mite populations. Additionally, avoiding over-fertilization with nitrogen-rich fertilizers can help discourage mite infestations.<br><br>
        <strong>Biological Control:</strong> Predatory mites, such as <i>Phytoseiulus persimilis</i>, can be introduced to tomato plants to feed on spider mites and help control their populations.<br><br>
        <strong>Chemical Control:</strong> Insecticidal soaps, neem oil, or horticultural oils can be applied to tomato plants to smother and kill spider mites. Additionally, acaricides specifically targeting mites can be used, but care must be taken to avoid harming beneficial insects and pollinators.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Prevention</h2>
        <p>Regular monitoring of tomato plants for early signs of spider mite infestation, particularly during dry and hot weather conditions, can help prevent widespread damage. Implementing integrated pest management strategies, including cultural, biological, and chemical control methods, can effectively manage spider mite populations and minimize crop damage.</p>
        """
        ,
        
        'Tomato___Target_Spot': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Tomato Target Spot</u>.</h2>
        <p><strong>Tomato Target Spot</strong>, caused by the fungus <i>Corynespora cassiicola</i>, is a foliar disease that affects tomato plants. While not as common as some other tomato diseases, it can still cause significant damage under favorable conditions.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of tomato target spot typically include circular to irregularly shaped lesions on the leaves, which may have a concentric ring pattern, resembling a target. These lesions can vary in color from light brown to dark brown or black and may be surrounded by a yellow halo. Severe infections can lead to defoliation and reduced plant vigor.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Cultural Practices:</strong> Proper sanitation, including removal and destruction of infected plant material, can help reduce inoculum and slow the spread of target spot within the tomato field. Crop rotation with non-host crops can also help break the disease cycle.<br><br>
        <strong>Fungicide Application:</strong> Regular application of fungicides, particularly those containing active ingredients such as chlorothalonil or mancozeb, can help manage target spot in tomato crops. Application timing and frequency should follow label instructions and be based on disease pressure and environmental conditions.<br><br>
        <strong>Resistant Varieties:</strong> Planting tomato cultivars with genetic resistance to target spot can provide effective control of the disease. Resistant varieties may exhibit fewer symptoms and require fewer fungicide applications.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Tomato target spot is caused by the fungus <i>Corynespora cassiicola</i>. The fungus can survive in infected plant debris and soil, spreading to new plants through wind-driven rain, splashing water, or mechanical means. Optimal conditions for disease development include warm temperatures ranging from 75°F to 85°F (24°C to 29°C) and high humidity. Overhead irrigation or frequent rainfall can exacerbate disease spread.</p>
        """
        ,
        
        'Tomato___Tomato_Yellow_Leaf_Curl_Virus': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Tomato Yellow Leaf Curl Virus</u>.</h2>
        <p><strong>Tomato Yellow Leaf Curl Virus (TYLCV)</strong> is a viral disease that affects tomato plants, causing significant damage to crops worldwide. It belongs to the genus <i>Begomovirus</i> and is transmitted by the whitefly <i>Bemisia tabaci</i>.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of Tomato Yellow Leaf Curl Virus typically include yellowing and upward curling of the leaves, along with stunted growth and reduced fruit yield. Infected plants may also exhibit leaf thickening, puckering, and vein clearing. Fruit development may be impaired, with small and distorted fruits being common.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Vector Control:</strong> Managing populations of the whitefly vector, <i>Bemisia tabaci</i>, is crucial for preventing the spread of TYLCV. This can be achieved through the use of insecticides targeting whiteflies and by implementing cultural control practices such as removing weed hosts.<br><br>
        <strong>Resistant Varieties:</strong> Planting tomato cultivars that are resistant or tolerant to TYLCV can help reduce the impact of the disease on crops. Resistant varieties can withstand virus infection better and may exhibit fewer symptoms.<br><br>
        <strong>Cultural Practices:</strong> Good crop management practices, including proper sanitation, crop rotation, and removal of infected plants, can help reduce the spread of TYLCV within the tomato field.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Tomato Yellow Leaf Curl Virus is caused by a group of viruses belonging to the genus <i>Begomovirus</i>. The virus is transmitted by the whitefly vector, <i>Bemisia tabaci</i>, in a persistent, circulative manner. Infected whiteflies acquire the virus from infected plants and transmit it to healthy plants during feeding. TYLCV can also spread through infected seed and plant material.</p>
        """
        ,
        
        'Tomato___Tomato_mosaic_virus': 
        """
        <h2 style="font-weight: bold; font-size: 26px; text-align: center;">Detected disease is <u>Tomato Mosaic Virus</u>.</h2>
        <p><strong>Tomato Mosaic Virus (ToMV)</strong> is a viral disease that affects tomato plants, causing significant damage to crops worldwide. It belongs to the genus <i>Tobamovirus</i> and can lead to reduced yield and fruit quality.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Symptoms</h2>
        <p>The symptoms of Tomato Mosaic Virus typically include mosaic patterns of light and dark green on the leaves, along with leaf curling, distortion, and stunting. Infected plants may also exhibit yellowing, wilting, and necrosis of foliage. Fruit development may be impaired, with mottling, distortion, and reduced size.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Preventive Measures</h2>
        <p><strong>Seed Treatment:</strong> Using virus-free seed and certified disease-free transplants can help prevent the introduction of ToMV into tomato crops.<br><br>
        <strong>Vector Control:</strong> Implementing measures to control aphids, which can transmit ToMV, can help reduce the spread of the virus. Insecticides targeting aphids and cultural control practices such as removing weed hosts can be effective.<br><br>
        <strong>Cultural Practices:</strong> Good crop management practices, including proper sanitation, crop rotation, and removal of infected plants, can help reduce the spread of ToMV within the tomato field.</p>
        <h2 style="font-weight: bold; font-size: 23px; ">Causes</h2>
        <p>Tomato Mosaic Virus is caused by the <i>Tomato mosaic virus</i> belonging to the genus <i>Tobamovirus</i>. It can be transmitted through infected seed, plant debris, and mechanical means such as contaminated tools and hands. Aphids can also vector the virus from infected to healthy plants during feeding.</p>
        """
        ,
        
        'Tomato___healthy': """<h2 style="font-weight: bold; font-size: 26px; text-align: center;">Your crop is healthy🥳</h2>"""
    }
    
    # Get the corresponding text for the given disease
    return disease_to_text.get(disease, "Additional text not available")
