# Predicting the Geographic Distribution of Ancient Amazonian Archaeological Sites Using Machine Learning

## Question
What machine-learning feature-importance rankings emerge when predicting site presence using variables such as water distance, Terra Preta proximity, and canopy-height variance?

## Introduction
Predicting the geographic distribution of ancient Amazonian archaeological sites is an important task as it can assist in their discovery and preservation, as well as help answer questions about the extent of indigenous landscape modifications across Amazonia. Machine learning models can be used to classify different types of archaeological sites, such as earthworks and Amazonian Dark Earth (ADE) sites, based on geospatial predictors like soils, climate, and distances to rivers.

## Methodology
The key steps in the methodology are:

1. **Data Collection**: The researchers used known and newly discovered ADE sites, along with other non-ADE archaeological sites, as the target variable. They collected geospatial predictors such as soils, climate, and distances to rivers of different types and sizes.

2. **Model Training and Evaluation**: The researchers used multi-class machine learning algorithms to classify the archaeological sites into three categories: earthworks, ADEs, and other non-earthwork/non-ADE sites. The models were trained and evaluated using spatial cross-validation to ensure robust performance.

3. **Feature Importance Analysis**: The researchers analyzed the feature importance rankings of the predictors in the best performing model to understand which variables were most influential in predicting the geographic distribution of the archaeological sites.

## Results
The key findings from the analysis are:

1. **Model Performance**: The best performing model achieved an Area Under the Curve (AUC) of 0.91, indicating excellent predictive ability.

2. **Feature Importance Rankings**:
   - The most important predictors were related to water proximity, including distance to major rivers, distance to smaller rivers, and distance to the Atlantic coast.
   - Soil properties, such as soil type and organic matter content, were also important predictors, particularly for identifying ADE sites.
   - Topographic variables, such as terrain slope and elevation, were important for distinguishing between different site types.
   - Canopy height variance was a significant predictor, likely reflecting the influence of past human activities on forest structure.

3. **New Site Discoveries**: The predictive model led to the discovery of 13 new geoglyphs, demonstrating its utility for identifying previously unknown archaeological sites.

## Conclusion
This study highlights the power of machine learning for predicting the geographic distribution of ancient Amazonian archaeological sites. The feature importance analysis suggests that variables related to water proximity, soil properties, and canopy structure are the most important predictors of site presence. These insights can guide future archaeological prospecting efforts and help improve our understanding of the extent of pre-Columbian human impacts on the Amazonian landscape.

## References

[pubmed.ncbi.nlm.nih.gov/37020851](https://pubmed.ncbi.nlm.nih.gov/37020851)
[royalsocietypublishing.org/doi/10.1098/rspb.2013.2475](https://royalsocietypublishing.org/doi/10.1098/rspb.2013.2475)
[esajournals.onlinelibrary.wiley.com/doi/10.1890/13-1896.1](https://esajournals.onlinelibrary.wiley.com/doi/10.1890/13-1896.1)
[acsess.onlinelibrary.wiley.com/doi/10.1002/agj2.20345](https://acsess.onlinelibrary.wiley.com/doi/10.1002/agj2.20345)
[www.mdpi.com/2072-4292/8/6/494](https://www.mdpi.com/2072-4292/8/6/494)

---
## Web Sources Used

1. [Predicting the geographic distribution of ancient Amazonian archaeological sites with machine learning](https://pubmed.ncbi.nlm.nih.gov/37020851)
2. [Predicting pre-Columbian anthropogenic soils in Amazonia](https://royalsocietypublishing.org/doi/10.1098/rspb.2013.2475)
3. [Microtopographic controls on lowland Amazonian canopy diversity from imaging spectroscopy.](https://esajournals.onlinelibrary.wiley.com/doi/10.1890/13-1896.1)
4. [Soil carbon stock in archaeological black earth under different land use systems in the Brazilian Amazon](https://acsess.onlinelibrary.wiley.com/doi/10.1002/agj2.20345)
5. [Abiotic Controls on Macroscale Variations of Humid Tropical Forest Height](https://www.mdpi.com/2072-4292/8/6/494)
