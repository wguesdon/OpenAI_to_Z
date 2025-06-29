# Integrating Hydrology, Soils, and Cultural Distance in Multi-Criteria Suitability Models to Rank Unexplored Polygons for Survey Priority

**Question Restated:**  
How can multi-criteria suitability models (AHP, MaxEnt, or Bayesian networks) integrate hydrology, soils, and cultural distance to rank unexplored polygons for survey priority?

---

## Introduction

Prioritizing unexplored polygons for surveys in fields like environmental planning, archaeology, or land use often requires the integration of diverse and complex datasets, such as hydrological features, soil characteristics, and cultural factors. Multi-criteria suitability models such as Analytic Hierarchy Process (AHP), Maximum Entropy (MaxEnt), and Bayesian networks provide structured frameworks for synthesizing these heterogeneous data into a meaningful ranking. This report details how these methods can be leveraged specifically for integrating hydrology, soils, and cultural distance, thus enhancing decision-making for survey prioritization.

---

## Overview of Multi-Criteria Suitability Models

### 1. **Analytic Hierarchy Process (AHP)**
- **Nature:** AHP is a structured technique based on pairwise comparisons and hierarchical weighting of criteria.
- **Mechanism:** It assigns weights to each criterion based on their relative importance and aggregates them into a composite suitability score.
- **Suitability:** Particularly useful when expert knowledge is available to prioritize qualitative and quantitative criteria.
  
### 2. **Maximum Entropy Model (MaxEnt)**
- **Nature:** MaxEnt is a machine learning model that estimates probability distributions with maximum entropy given presence-only data.
- **Mechanism:** It uses environmental and spatial covariates to model suitability or occurrence probability across a landscape.
- **Suitability:** Useful for ecological or landscape spatial modeling based on multiple spatial predictors without requiring absence data.

### 3. **Bayesian Networks (BN)**
- **Nature:** BN are probabilistic graphical models representing variables and their conditional dependencies.
- **Mechanism:** They integrate prior knowledge and observed data to update beliefs about suitability or risk in spatial units.
- **Suitability:** Effective for modeling uncertainties and complex causal relationships among variables.

---

## Integrating Hydrology, Soils, and Cultural Distance Into Models

### Key Data Types:
- **Hydrology:** Data on water bodies, drainage density, flood risk, soil moisture, etc.
- **Soils:** Soil type, texture, fertility, drainage, erosion risk.
- **Cultural distance:** Measures of proximity to cultural sites, historical significance, community access, or intangible cultural landscapes.

---

## Model-Specific Integration Approaches

### 1. **AHP Integration**
- **Criteria Selection:** Define criteria layers — hydrological suitability, soil fertility, and cultural distance.
- **Pairwise Comparisons:** Experts perform pairwise comparisons to assign relative importance (weights) to hydrology, soils, and cultural criteria.
- **Normalization and Scoring:** Each polygon gets scored on every criterion using spatial data; e.g., soil type suitability maps, hydrology maps, and cultural proximity maps.
- **Weighted Overlay:** Scores are combined using weighted sums to produce a final suitability score per polygon.
- **Ranking:** Polygons ranked by their composite scores to identify high-priority survey areas.
  
**Advantages:** Incorporates expert judgment explicitly; transparent weighting.

**Example Usage:** The hierarchical structure can include sub-criteria (e.g., within soils: pH, organic matter) to refine suitability assessments [link.springer.com PDF](https://link.springer.com/content/pdf/10.1007/s13201-022-01618-2.pdf).

---

### 2. **MaxEnt Integration**
- **Input Variables:** Raster layers representing hydrological variables (e.g., distance to water), soil characteristics, and cultural distance indicators.
- **Presence Data:** Known surveyed or relevant "presence" points to train MaxEnt.
- **Model Execution:** MaxEnt estimates probability distribution maximizing entropy under constraints imposed by environmental predictors.
- **Prediction:** Outputs a suitability probability map predicting priority survey polygons.
  
**Advantages:** Handles continuous and categorical data, effective with presence-only data, provides variable contribution analysis.

**Example Usage:** MaxEnt has been used in land suitability to integrate environmental variables for prioritizing land use [mdpi.com article](https://www.mdpi.com/2073-445X/14/4/775).

---

### 3. **Bayesian Networks Integration**
- **Structure:** Define nodes for hydrology, soils, cultural distance, and survey priority.
- **Conditional Probability Tables:** Quantify relationships (e.g., probability of survey priority given certain soil and hydrology classes and cultural distance).
- **Data Integration:** Use spatial data and expert knowledge to parameterize the model.
- **Inference:** Propagate uncertainties and update beliefs about each polygon’s survey priority.
- **Output:** Probabilistic ranking of polygons for survey priority reflecting both data and uncertainty.
  
**Advantages:** Captures probabilistic dependencies and manages uncertainties in data and criteria integration.

---

## Workflow for Ranking Polygons

1. **Data Collection:**
   - Hydrological maps (drainage, water presence, flood risks).
   - Soil surveys or remote sensing soil characteristics.
   - Cultural datasets (site locations, cultural distance metrics).
   
2. **Preprocessing:**
   - Rasterize or vectorize data into uniform spatial units (polygons).
   - Standardize data to comparable scales.
   
3. **Criteria Weighting and Modeling:**
   - For AHP: Conduct expert pairwise weighting.
   - For MaxEnt: Use presence data to train.
   - For Bayesian networks: Build conditional probability tables.
   
4. **Integration and Scoring:**
   - Calculate scores or probabilities for each polygon.
   
5. **Ranking and Decision Making:**
   - Rank polygons based on composite suitability.
   - Select top-ranked polygons for survey prioritization.

---

## Additional Considerations

- **Multi-Data Type Fusion:** Use GIS platforms to integrate spatial datasets with attribute data effectively.
- **Hybrid Approaches:** Combine methods, e.g., use AHP for weighting criteria before feeding layers into MaxEnt or Bayesian network.
- **Validation:** Use ground truth or expert validation where possible to refine models.
- **Incorporation of Socioeconomic Factors:** Expand cultural distance to include social-economic influences if relevant, improving model robustness [MDPI Sustainability](https://www.mdpi.com/2071-1050/17/9/4130).

---

## Conclusion

Multi-criteria suitability models like AHP, MaxEnt, and Bayesian networks can effectively integrate hydrology, soils, and cultural distance to rank unexplored polygons for survey priority by:

- Using hierarchical weighting and scoring (AHP)
- Estimating spatial suitability probability from environmental predictors (MaxEnt)
- Modeling probabilistic dependencies among multiple criteria (Bayesian networks)

These approaches enable decision-makers to prioritize areas with the highest likelihood or suitability for survey, optimizing resource allocation and increasing survey effectiveness.

---

## References

- Luo, K. (2025). *Evaluation of Land Suitability for Construction in the Turpan–Hami Region Based on the Integration of the MaxEnt Model and Regional Planning*. MDPI Land. [mdpi.com](https://www.mdpi.com/2073-445X/14/4/775)
- Hagos, Y. G., et al. (2022). *Land suitability assessment for surface irrigation development at Ethiopian highlands using geospatial technology*. Springer. [link.springer.com PDF](https://link.springer.com/content/pdf/10.1007/s13201-022-01618-2.pdf)
- Benavides-Bolaños, J. A. (2025). *Integrating AHP and GIS for Sustainable Surface Water Planning: Identifying Vulnerability to Agricultural Diffuse Pollution in the Guachal River Watershed*. MDPI Sustainability. [mdpi.com](https://www.mdpi.com/2071-1050/17/9/4130)
- Mendonça, G. C., et al. (2023). *Multicriteria spatial model to prioritize degraded areas for landscape restoration through agroforestry*. PubMed. [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/36911210)

---

This structured approach promotes rigorous integration of multi-disciplinary spatial data into effective prioritization schemas using advanced suitability modeling techniques.

---
## Web Sources Used

1. [Evaluation of Land Suitability for Construction in the Turpan–Hami Region Based on the Integration of the MaxEnt Model and Regional Planning](https://www.mdpi.com/2073-445X/14/4/775)
2. [Multicriteria spatial model to prioritize degraded areas for landscape restoration through agroforestry](https://pubmed.ncbi.nlm.nih.gov/36911210)
3. [Land suitability assessment for surface irrigation development at Ethiopian highlands using geospatial technology](https://link.springer.com/content/pdf/10.1007/s13201-022-01618-2.pdf)
4. [Integrating AHP and GIS for Sustainable Surface Water Planning: Identifying Vulnerability to Agricultural Diffuse Pollution in the Guachal River Watershed](https://www.mdpi.com/2071-1050/17/9/4130)
5. [Evaluation of Land Suitability Methods with Reference to Neglected and Underutilised Crop Species: A Scoping Review](https://www.mdpi.com/2073-445X/10/2/125)
