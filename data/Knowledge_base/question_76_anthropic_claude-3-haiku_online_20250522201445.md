# Integrating Multiple Factors for Survey Priority Ranking

## Question Restatement
How can multi-criteria suitability models (AHP, MaxEnt, or Bayesian networks) integrate hydrology, soils, and cultural distance to rank unexplored polygons for survey priority?

## Introduction
Determining survey priorities for unexplored areas is a crucial step in optimizing field research and resource allocation. Multi-criteria suitability models offer a robust approach to integrate diverse factors, such as hydrology, soils, and cultural distance, to rank these polygons based on their suitability for further investigation. This report explores how AHP (Analytic Hierarchy Process), MaxEnt (Maximum Entropy), and Bayesian networks can be employed to tackle this challenge.

## Analytic Hierarchy Process (AHP)
The AHP method involves structuring the decision problem into a hierarchy, with the overall goal at the top, and the relevant criteria and sub-criteria nested below. [mdpi.com](https://www.mdpi.com/2073-445X/14/4/775) demonstrates the use of AHP to evaluate land suitability for construction, considering factors such as terrain, hydrology, and soil conditions. This approach can be adapted to rank unexplored polygons for survey priority by:

1. Identifying the key criteria (hydrology, soils, cultural distance) and their relative importance through pairwise comparisons.
2. Assigning weights to each criterion based on the pairwise comparisons.
3. Scoring each unexplored polygon against the criteria and aggregating the scores to obtain a final suitability ranking.

## Maximum Entropy (MaxEnt)
The MaxEnt model is a machine learning approach that can effectively integrate multiple environmental and socioeconomic variables to predict the suitability of a location for a given purpose. [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/36911210) demonstrates the use of MaxEnt to prioritize degraded areas for landscape restoration through agroforestry, considering factors like soil quality and cultural influences. This model can be adapted to rank unexplored polygons by:

1. Compiling a dataset of the relevant factors (hydrology, soils, cultural distance) for the study area.
2. Training the MaxEnt model using the dataset to generate a suitability map for the unexplored polygons.
3. Ranking the polygons based on their predicted suitability scores.

## Bayesian Networks
Bayesian networks are probabilistic graphical models that can effectively integrate various types of data, including quantitative and qualitative, to make informed decisions. [www.mdpi.com](https://www.mdpi.com/2073-4441/17/7/1045) presents the use of Bayesian networks to evaluate homogeneous areas for rainfed wheat yield assessment, considering factors such as climate and soil characteristics. This approach can be adapted to rank unexplored polygons by:

1. Constructing a Bayesian network that incorporates the relevant factors (hydrology, soils, cultural distance).
2. Defining the conditional probability distributions between the variables in the network.
3. Propagating the evidence through the network to calculate the posterior probabilities of each unexplored polygon, which can then be used to rank them.

## Conclusion
Multi-criteria suitability models, such as AHP, MaxEnt, and Bayesian networks, offer a powerful approach to integrating diverse factors, including hydrology, soils, and cultural distance, to rank unexplored polygons for survey priority. By leveraging the strengths of these methods, researchers and decision-makers can optimize field investigations and resource allocation, leading to more efficient and informed decision-making processes.

## References
[1] Luo, K. (2025). Evaluation of Land Suitability for Construction in the Turpan–Hami Region Based on the Integration of the MaxEnt Model and Regional Planning. *Land*, 14(4), 775. [https://www.mdpi.com/2073-445X/14/4/775](https://www.mdpi.com/2073-445X/14/4/775)

[2] de Mendonça, G. C., da Costa, L. M., Abdo, M. T. V. N., Costa, R. C. A., Parras, R., de Oliveira, L. C. M., ... & Pacheco, F. A. L. (2023). Multicriteria spatial model to prioritize degraded areas for landscape restoration through agroforestry. *PubMed*, 36911210. [https://pubmed.ncbi.nlm.nih.gov/36911210](https://pubmed.ncbi.nlm.nih.gov/36911210)

[3] Mugiyo, H., Chimonyo, V. G. P., Sibanda, M., Kunz, R., Masemola, C. R., Modi, A. T., & Mabhaudhi, T. (2021). Evaluation of Land Suitability Methods with Reference to Neglected and Underutilised Crop Species: A Scoping Review. *Land*, 10(2), 125. [https://www.mdpi.com/2073-445X/10/2/125](https://www.mdpi.com/2073-445X/10/2/125)

[4] Hao, S. (2025). GA-Optimized Sampling for Soil Type Mapping in Plain Areas: Integrating Legacy Maps and Multisource Covariates. *Agronomy*, 15(4), 963. [https://www.mdpi.com/2073-4395/15/4/963](https://www.mdpi.com/2073-4395/15/4/963)

[5] Firozjaei, M. K. (2025). A Spatial Multi-Criteria Decision-Making Approach to Evaluating Homogeneous Areas for Rainfed Wheat Yield Assessment. *Water*, 17(7), 1045. [https://www.mdpi.com/2073-4441/17/7/1045](https://www.mdpi.com/2073-4441/17/7/1045)

---
## Web Sources Used

1. [Evaluation of Land Suitability for Construction in the Turpan–Hami Region Based on the Integration of the MaxEnt Model and Regional Planning](https://www.mdpi.com/2073-445X/14/4/775)
2. [Multicriteria spatial model to prioritize degraded areas for landscape restoration through agroforestry](https://pubmed.ncbi.nlm.nih.gov/36911210)
3. [Evaluation of Land Suitability Methods with Reference to Neglected and Underutilised Crop Species: A Scoping Review](https://www.mdpi.com/2073-445X/10/2/125)
4. [GA-Optimized Sampling for Soil Type Mapping in Plain Areas: Integrating Legacy Maps and Multisource Covariates](https://www.mdpi.com/2073-4395/15/4/963)
5. [A Spatial Multi-Criteria Decision-Making Approach to Evaluating Homogeneous Areas for Rainfed Wheat Yield Assessment](https://www.mdpi.com/2073-4441/17/7/1045)
