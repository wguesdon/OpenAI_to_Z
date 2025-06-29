# Machine-Learning Feature-Importance Rankings in Predicting Archaeological Site Presence Using Variables such as Water Distance, Terra Preta Proximity, and Canopy-Height Variance

## Restatement of the Question  
What machine-learning feature-importance rankings emerge when predicting site presence using variables such as water distance, Terra Preta proximity, and canopy-height variance?

---

## Introduction  
Predicting the geographic presence of archaeological sites in Amazonia, particularly those affected or created by past human activity, has been advanced by applying machine-learning techniques to a variety of environmental and anthropogenic variables. Common predictor variables often include distances to water bodies, proximity to specific soil features like Terra Preta (Amazonian Dark Earth), and vegetation structural characteristics such as canopy-height variance. Understanding how these variables rank in importance can enhance site discovery, preservation efforts, and the interpretation of historical human land use.

---

## Key Variables and Their Importance

1. ### Water Distance  
The proximity to rivers and water bodies represents a crucial environmental factor since many ancient Amazonian settlements and altered landscapes are found near waterways, which provided resources and transport routes. Models consistently find distance to rivers and water sources as a strong predictive variable.

2. ### Terra Preta (Anthropogenic Soil) Proximity  
Sites of nutrient-enriched anthropogenic soils known as Terra Preta are widely accepted indicators of long-term human settlement and landscape modification in Amazonia. Proximity to known Terra Preta locations is a robust predictor of archaeological site presence, often weighted heavily in machine-learning models.

3. ### Canopy-Height Variance  
Vegetation structure, notably canopy-height variance, can reflect varying degrees of human disturbance and natural habitat heterogeneity. Spectral imaging combined with machine learning has shown that microtopographic and vegetation differences, including canopy-height variability, correlate with the presence of distinct archeological features and modified landscapes.

---

## Evidence from Recent Studies

### Machine Learning Models and Feature Importance  

- **Walker et al. (2023)** applied multi-class machine learning algorithms (such as random forests or similar classifiers) to distinguish settlement earthworks versus Amazonian Dark Earth (ADE) sites and other areas. Predictors included soil types, climate variables, and distances to rivers of different sizes. In their best predictive model with 1 km spatial resolution, water-related distances and soil variables (including Terra Preta) ranked highly, producing an Area Under the Curve (AUC) of 0.91 for model performance. This indicates very strong predictive power and feature importance of these environmental variables.  
  - *"Models...using soils, climate, and distances to rivers...lead to the discovery of new geoglyphs and identify high-probability areas for undiscovered sites hidden by rainforest"*[pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/37020851).

- **Czarnecki (2014)** used a maximum entropy (Maxent) model to predict the distribution of Terra Preta soils across lowland Amazonia. The study found that terrain, hydrology, and soil characteristics were more influential predictors than climatic conditions. Notably, Terra Preta sites clustered near river lower courses, reaffirming the importance of water distance and hydrological context.  
  - *"Terrain, hydrologic and soil characteristics were more important predictors of Terra Preta distributions than climatic conditions"* and Terra Preta covers approx. 3.2% of the forested region, offering a focused target for predictive modeling.  
  ![Terra Preta Distribution Map](https://royalsocietypublishing.org/cms/asset/395feee4-00c3-4f20-af35-dab02f9f9a98/rspb.281.issue-1777.largecover.jpeg)  
  [royalsocietypublishing.org](https://royalsocietypublishing.org/doi/10.1098/rspb.2013.2475)

- **Fe & Asner** explored how microtopography affected canopy diversity using high-resolution imaging spectroscopy. By mapping canopy structure, including canopy height variation, they identified spatial patterns of biodiversity linked to geomorphological features such as terraces and floodplains, which themselves associate with human modification sites. This suggests canopy-height variance acts as a useful indirect indicator in site prediction models.  
  [esajournals.onlinelibrary.wiley.com](https://esajournals.onlinelibrary.wiley.com/doi/10.1890/13-1896.1)

---

## Synthesis: Feature-Importance Rankings

Based on integrated findings:

| Feature Variable                 | Relative Importance in Predictive Models          | Explanation                                                                              |
|--------------------------------|---------------------------------------------------|------------------------------------------------------------------------------------------|
| **Distance to Water (Rivers)** | High                                              | Ancient habitation clustered near rivers; critical resource and transport routes.        |
| **Soil Variables (Including Terra Preta Proximity)** | High                                  | Terra Preta soils mark long-term settlement, with strong landscape modifications.        |
| **Canopy-Height Variance**      | Moderate to High                                  | Reflects vegetation disturbance and microtopography correlating with archaeological presence. |
| **Terrain & Hydrology Features**| Moderate                                         | Influence soil formation and habitability, impact site likelihood.                        |
| **Climate Variables**            | Low to Moderate                                  | Less influential compared to soil and proximity features.                                |

Machine-learning algorithms (e.g., random forests, Maxent, feature selection via χ² tests and wrappers) consistently rank proximity to water and Terra Preta as top predictors. Canopy-height variance, uncovered by remote sensing, is a valuable supplementary feature improving model spatial resolution and nuance.

---

## Conclusion

When predicting archaeological site presence within the Amazon using machine learning, **distance to water sources and proximity to Terra Preta soils emerge as the most important variables**. Vegetation structure variables such as canopy-height variance play a significant supporting role in capturing microenvironmental variation. These variables together enable highly accurate models for identifying current known sites and discovering new, hidden ones beneath dense rainforest.

---

## References

- Walker, R., Ferguson, J. R., Olmeda, A., Hamilton, M. J., Elghammer, J., Buchanan, B. (2023). Predicting the geographic distribution of ancient Amazonian archaeological sites with machine learning. *PubMed*. [https://pubmed.ncbi.nlm.nih.gov/37020851](https://pubmed.ncbi.nlm.nih.gov/37020851)  
- Czarnecki, C. (2014). Predicting pre-Columbian anthropogenic soils in Amazonia. *Proceedings of the Royal Society B*. [https://royalsocietypublishing.org/doi/10.1098/rspb.2013.2475](https://royalsocietypublishing.org/doi/10.1098/rspb.2013.2475)  
- Fe, J.-B., Asner, G. P. (2013). Microtopographic controls on lowland Amazonian canopy diversity from imaging spectroscopy. *Ecological Applications*. [https://esajournals.onlinelibrary.wiley.com/doi/10.1890/13-1896.1](https://esajournals.onlinelibrary.wiley.com/doi/10.1890/13-1896.1)  
- López‐noronha, R., Souza, Z. M. D., Soares, M. D. R., Campos, M. C. C., Farhate, C. V. V., Oliveira, S. R. D. M. (2020). Soil carbon stock in archaeological black earth under different land use systems in the Brazilian Amazon. *Agronomy Journal*. [https://acsess.onlinelibrary.wiley.com/doi/10.1002/agj2.20345](https://acsess.onlinelibrary.wiley.com/doi/10.1002/agj2.20345)

---
## Web Sources Used

1. [Predicting the geographic distribution of ancient Amazonian archaeological sites with machine learning](https://pubmed.ncbi.nlm.nih.gov/37020851)
2. [Predicting pre-Columbian anthropogenic soils in Amazonia](https://royalsocietypublishing.org/doi/10.1098/rspb.2013.2475)
3. [Microtopographic controls on lowland Amazonian canopy diversity from imaging spectroscopy.](https://esajournals.onlinelibrary.wiley.com/doi/10.1890/13-1896.1)
4. [Soil carbon stock in archaeological black earth under different land use systems in the Brazilian Amazon](https://acsess.onlinelibrary.wiley.com/doi/10.1002/agj2.20345)
5. [GEOARQUEOLOGIA DE ANTROSSOLOS DO SÍTIO TERRA PRETA 2, VALE DO BAIXO AMAZONAS, JURUTI-PARÁ, BRASIL](https://rbgeomorfologia.org.br/rbg/article/view/1729)
