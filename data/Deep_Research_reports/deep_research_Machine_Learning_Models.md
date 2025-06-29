# Machine Learning Models for Detecting Hidden Amazonian Archaeology (2015–2025)
Original Question: Identify machine learning models that have successfully been used between 2015 and 2025 to detect archaeological features hidden beneath forest canopy in the Brazilian Amazon. Emphasize approaches that utilize remote sensing technologies, such as LiDAR, synthetic aperture radar (SAR), and multispectral or hyperspectral imagery. ## Machine Learning Models and Approaches
- Random Forest (Ensemble Tree Classifier): Random forests have been a top performer for predicting archaeological site locations in Amazonia. For example, a 2023 study trained a multi-class random forest to classify regions as containing earthworks (ancient enclosures), Amazonian Dark Earth (anthropogenic fertile soil), or no known site
pmc.ncbi.nlm.nih.gov
. The random forest outperformed neural networks, support vector machines, and gradient-boosted trees in this task
pmc.ncbi.nlm.nih.gov
. It leveraged dozens of remote-sensing-derived environmental layers (e.g. climate grids, elevation, soil properties) to predict site presence
pmc.ncbi.nlm.nih.gov
pmc.ncbi.nlm.nih.gov
. The best model achieved an AUC ≈0.91 in spatial cross-validation and even led researchers to discover 13 new pre-Columbian geoglyph sites in areas flagged as high-probability by the model
pmc.ncbi.nlm.nih.gov
. This underscores how ensemble classifiers can successfully highlight hidden archaeological hotspots under the Amazon jungle canopy. - Convolutional Neural Networks (CNNs): Deep learning with CNNs has been applied to remote sensing data for automatic feature detection. CNN-based algorithms excel at recognizing subtle patterns in complex imagery that may indicate human-made structures hidden by vegetation
avantglobal.ai
. For instance, researchers have used CNN models to analyze high-resolution aerial and satellite images, identifying geometric anomalies (e.g. straight lines, circular mounds) that stand out from natural forest patterns
avantglobal.ai
avantglobal.ai
. In one case outside Amazonia, a CNN detected ancient nomadic tombs from satellite photos
remars.amazonevents.com
, illustrating the approach’s potential. In the Amazon, similar CNN techniques can be applied on LiDAR-derived elevation maps or SAR imagery to pinpoint anthropogenic earthworks (like raised causeways or enclosures) beneath the canopy. These deep networks can learn the “signature” of archaeological features (regular shapes, distinct textures) and scan vast remote-sensing datasets far faster than manual eye-search, significantly accelerating discoveries in dense rainforest. - U-Net (Deep Learning Segmentation Network): U-Net – a type of CNN specialized for image segmentation – has been successfully used to map features in the Amazon’s forests. A notable example is using U-Net to identify canopy palm trees from remote sensing data, which can serve as proxies for human activity. Wagner et al. (2020) employed a U-Net model on very-high-resolution (0.5 m) multispectral imagery (GeoEye satellite) to automatically segment and map individual palm crowns across ~3,000 km² of Amazon forest
mdpi.com
. The deep model learned the unique star-shaped crown appearance of certain palms and achieved ~95% mapping accuracy (F1 ≈0.7) in dense forest
mdpi.com
. Similarly, Dal’Agnol da Silva et al. (2022) used a U-Net on airborne LiDAR data (0.5 m canopy height models) to detect over 1.1 million palm tree segments in 480,000 ha of Amazonia
researchgate.net
researchgate.net
. These palms (e.g. Mauritia flexuosa) often thrive on anthropogenic soils or in old settlement areas, so their distribution can signal ancient human-modified landscapes. By training on manually labeled examples, the U-Net learned to “see through” the canopy and delineate features of interest – showcasing how deep segmentation networks can reveal archaeological indicators (like culturally-important plant species or micro-topographic features) hidden in the Amazon forest. - Support Vector Machines & Other Classifiers: Besides deep learning and trees, more traditional machine learning models have also been applied. Support Vector Machine (SVM) classifiers and logistic regression have been tested for detecting Amazonian archaeological zones, though with mixed success
pmc.ncbi.nlm.nih.gov
. For example, early work used MaxEnt (Maximum Entropy) modeling – a machine-learning method for presence-only data – to predict fertile terra preta soil sites across Amazonia based on environmental predictors. This approach identified likely zones for undiscovered anthropogenic soils accounting for ~3.2% of the Amazon basin
scholars.unh.edu
, providing targets for future surveys “under the vast forest canopy”
scholars.unh.edu
. Likewise, object-based image analysis (OBIA), which combines image segmentation with machine learning, has been employed on LiDAR data to automatically recognize man-made earthworks (such as circular mound complexes) by their shape and reflective characteristics
remars.amazonevents.com
remars.amazonevents.com
. While algorithms like SVM or OBIA rules can detect certain features, in practice they are often outshined by ensemble methods (like Random Forest) or deep CNNs in terms of accuracy. Nonetheless, they have contributed to successful case studies, and their continued refinement (often in hybrid workflows) helps flag potential archaeological anomalies in remote sensing datasets. ## Notable Applications in the Brazilian Amazon (2015–2025)


LiDAR-derived 3D terrain model of an ancient Amazonian settlement (Cotoca site, in the Bolivian Amazon) hidden under forest canopy. Features like rectangular plaza mounds, a conical pyramid (right, in red), and linear causeways (extending to the edges) become visible once dense jungle vegetation is digitally removed
smithsonianmag.com
. Such remote-sensing breakthroughs have revealed that parts of the Amazon were extensively engineered by pre-Columbian societies. - LiDAR Discovery of “Lost” Settlements: Airborne LiDAR (Light Detection and Ranging) has been a game-changer in Amazonian archaeology. In 2022–2023, researchers flew LiDAR surveys over remote forest in southwestern Amazonia and uncovered multiple large settlements beneath the canopy
english.elpais.com
english.elpais.com
. One Science study (Peripato et al. 2023) mapped 24 new pre-Columbian earthworks – including mounded villages, causeways, canals, and reservoirs – in just a 5,315 km² area (only 0.08% of the basin)
english.elpais.com
. By combining these LiDAR findings with a spatial prediction model, they estimated on the order of 10,000–23,000 archaeological sites still remain undiscovered under Amazon forest cover
rainfor.org
rainfor.org
. Most of these hidden sites are predicted in the southwestern Amazon, a region now recognized as a major center of ancient urbanism. This LiDAR+ML approach dramatically revises our understanding of Amazonian settlement density and guides future surveys to the highest-probability areas. - Predictive Modeling of Site Distribution: Machine learning models are also helping pinpoint likely site locations across the vast Amazon when LiDAR data are unavailable. Walker et al. (2023) built a random forest model using climate, terrain, hydrology and soil layers to predict where earthworks or Amazonian Dark Earth (ADE) are likely to occur
pmc.ncbi.nlm.nih.gov
pmc.ncbi.nlm.nih.gov
. The model’s output was a probability map of site occurrence, essentially a treasure map for archaeologists. Significantly, this led to ground-truthing and discovery of new geoglyphs in Acre state that were previously unknown
pmc.ncbi.nlm.nih.gov
. Likewise, earlier statistical ML (MaxEnt) analysis of known ADE sites successfully highlighted environmental combinations (bluffs above rivers, certain soil types) where undiscovered ancient villages are likely
scholars.unh.edu
scholars.unh.edu
. These predictive models suggest that many archaeological features lie hidden beneath intact rainforest, but often in predictable patterns – for example, near fertile soils or water, and in regions with certain forest composition. By identifying those patterns, ML guides researchers where to “look” with high-resolution tools, even before any clearing or LiDAR takes place. - Vegetation as an Archaeological Indicator: Innovative studies in the late 2010s used machine learning on vegetation data to detect human influence. Because past Indigenous practices often enriched soils and encouraged useful plants, today’s forest canopy can betray ancient habitation. A 2022 deep learning study mapped canopy palms across Brazil’s Amazon and found over 1 billion palms, with distinct hotspots of palm density in the eastern and southwestern Amazon
researchgate.net
mdpi.com
. Some of these areas coincide with known pre-Columbian regions (e.g. Acre state’s geoglyph zone is a palm hotspot), hinting that humans fostered palm-rich forests. Additionally, Peripato et al. noted 53 tree species (like brazil nut, cacao, and fruit palms) are significantly over-represented around detected earthworks
rainfor.org
 – living evidence of prehistoric agroforestry. By using classifiers to map such “cultural indicator” species from satellite or LiDAR data, researchers can infer where ancient people altered the landscape. In essence, the Amazon’s botanical composition, when analyzed with ML, serves as a ghost record of past human presence lurking beneath the canopy. - Synthetic Aperture Radar (SAR) Anomaly Detection: SAR sensors (radar imaging satellites) penetrate clouds and some vegetation, providing another way to find hidden features. Between 2018 and 2025, teams have begun exploiting SAR data of the Amazon with machine learning to flag unnatural patterns. Algorithms can scan radar images for the telltale straight lines or geometric shapes of roads, ditches, or building foundations that differ from random natural textures
avantglobal.ai
avantglobal.ai
. For instance, researchers from Brazil’s space agency (INPE) are integrating SAR-based mapping to monitor deforestation and simultaneously watch for newly exposed archaeological remains as logging reveals them
avantglobal.ai
. Even under intact forest, SAR intensity and phase data can reflect subtle ground relief—ML models are being trained to pick out slight elevation changes or soil disturbances that correspond to things like ancient raised fields or causeway networks. While still emerging, these SAR+ML techniques have successfully identified a number of candidate sites, demonstrating the potential of radar for “seeing” through the canopy. As SAR coverage of the Amazon grows (e.g. Sentinel-1, ALOS-2), machine learning will play a crucial role in sifting the massive data for hidden archaeological signals. ## References
1. Walker, R.S. et al. (2023). Predicting the geographic distribution of ancient Amazonian archaeological sites with machine learning. PeerJ 11:e15137. DOI: 10.7717/peerj.15137
pmc.ncbi.nlm.nih.gov
pmc.ncbi.nlm.nih.gov
.
2. Peripato, V. et al. (2023). More than 10,000 pre-Columbian earthworks are still hidden throughout Amazonia. Science 382(6667):102–106. DOI: 10.1126/science.ade2541
rainfor.org
rainfor.org
.
3. Dal’Agnol da Silva, R. et al. (2022). Canopy palm cover across the Brazilian Amazon forests mapped with airborne LiDAR data and deep learning. Remote Sensing in Ecology and Conservation 8(5): 601–614. DOI: 10.1002/rse2.264
researchgate.net
researchgate.net
.
4. Wagner, F.H. et al. (2020). Regional Mapping and Spatial Distribution Analysis of Canopy Palms in an Amazon Forest Using Deep Learning and VHR Images. Remote Sensing 12(14): 2225. DOI: 10.3390/rs12142225
mdpi.com
mdpi.com
.
5. McMichael, C.H. et al. (2014). Predicting pre-Columbian anthropogenic soils in Amazonia. Proc. Royal Society B 281(1777): 20132475. DOI: 10.1098/rspb.2013.2475
scholars.unh.edu
scholars.unh.edu
.
6. Avant (Avant Global AI) (2023). Using SAR Technology to Identify Lost Historical Sites in the Amazon Rainforest (blog post)
avantglobal.ai
avantglobal.ai
.
7. Handwerk, B. (2022). Lost Cities of the Amazon Discovered From the Air. Smithsonian Magazine, May 25, 2022
smithsonianmag.com


.
