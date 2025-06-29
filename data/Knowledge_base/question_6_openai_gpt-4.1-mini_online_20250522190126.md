# Combining Radar, Hyperspectral, and LIDAR Data for Sub-Canopy Detection

**Question:**  
*How are radar (e.g., Sentinel-1 SAR) and hyperspectral data being combined with LIDAR for sub-canopy detection?*

---

## Introduction

Sub-canopy detection in forest and vegetation monitoring involves identifying elements beneath the upper vegetation canopy, such as understory plants, smaller trees, or ground features. This is challenging because the strength of signals from the top layers often dominates the remote sensing data.

Combining remote sensing technologies such as radar (e.g., Sentinel-1 SAR), hyperspectral imaging, and LIDAR has emerged as a promising approach to enhance sub-canopy detection. Each data source provides complementary information:

- **LIDAR** captures 3D structural details of vegetation, penetrating through canopy gaps to provide vertical profiles.
- **Hyperspectral data** delivers detailed spectral information linked to vegetation type, health, and biochemical properties.
- **Radar (SAR)** offers sensitivity to surface roughness, moisture content, and structure with the ability to penetrate some vegetation layers.

---

## Data Fusion to Improve Sub-Canopy Detection

### Complementarity of Data Types

- **Radar + Hyperspectral:**  
  Radar provides microwave backscatter sensitive to forest structure and moisture, while hyperspectral sensors capture fine spectral details of canopy and sub-canopy materials. Their combination improves discrimination of species and vegetative sub-layers that hyperspectral or radar alone may miss due to spectral mixing or scattering ambiguities.

- **LIDAR + Hyperspectral:**  
  LIDAR offers direct 3D structural data allowing differentiation of vertical vegetation layers and ground elevation, which hyperspectral alone cannot reveal. Hyperspectral data assist in species identification and health assessment. Research underscores the improvement in unmixing spectral signals and comprehensive interpretation by jointly using LIDAR and hyperspectral data, particularly for complex forest landscapes [sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S1367578821000110).

- **LIDAR + Radar:**  
  Radar data, such as Sentinel-1 SAR, have partial canopy penetration due to longer wavelengths, revealing sub-canopy structure especially when combined with the vertical resolution of LIDAR point clouds.

### Fusion Levels and Methods

The fusion of these datasets can be performed at different levels:

- **Low-level fusion (observation level):** Direct combination of raw sensed data, e.g., concatenating spectral bands and radar backscatter with LIDAR point cloud metrics.
- **Medium-level (feature level):** Extracting features from each data source, such as vegetation indices from hyperspectral, structural metrics from LIDAR, and texture or backscatter statistics from radar, then combining these features for analysis.
- **High-level (decision level):** Independently analyzing each data type and then combining classification or detection results through voting or ensemble approaches [sciencedirect.com](https://www.sciencedirect.com/science/article/pii/B9780444639776000134).

### Addressing Spectral Mixing and Sub-Canopy Complexity

Hyperspectral data can encounter challenges like spectral mixing, especially in semi-arid or dense environments where soil, litter, and cryptobiotic crust contribute to optical signals, obscuring sub-canopy classes. LIDAR's structural information and radar's penetration help overcome these issues by disentangling spectral signals according to vertical forest layers [mdpi.com](https://www.mdpi.com/2072-4292/11/18/2141/htm).

### Practical Applications

- **Tree Species Classification:** Combining UAV hyperspectral images with LiDAR point clouds enhances the distinction of canopy layers and improves species detection that exist mostly in the upper canopy but also influences sub-canopy interpretations [mdpi.com](https://www.mdpi.com/1999-4907/14/5/945).
- **Forest Monitoring:** UAV-acquired hyperspectral and LIDAR fusion along with multispectral and radar data supports monitoring large-scale forest changes and sub-canopy vegetation dynamics in complex environments [sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0034425717301578).

---

## Conclusion

The fusion of radar (e.g., Sentinel-1 SAR), hyperspectral, and LIDAR data leverages their complementary strengths to improve sub-canopy detection significantly. LIDAR provides vertical structure that helps separate canopy layers, hyperspectral data brings biochemical and species-level discrimination, and radar contributes structural and moisture-related information with partial canopy penetration. Fusion approaches at feature or decision levels are effectively used to integrate these datasets for enhanced detection and monitoring of sub-canopy vegetation and features.

---

## References

1. Li, S. (2021). A comprehensive review of hyperspectral data fusion with lidar and SAR data. *ISPRS Journal of Photogrammetry and Remote Sensing*.  
   [https://www.sciencedirect.com/science/article/pii/S1367578821000110](https://www.sciencedirect.com/science/article/pii/S1367578821000110)

2. Tusa, E., Laybros, A., Monnet, J.-M., et al. (2019). Fusion of hyperspectral imaging and LiDAR for forest monitoring. *ScienceDirect*.  
   [https://www.sciencedirect.com/science/article/pii/B9780444639776000134](https://www.sciencedirect.com/science/article/pii/B9780444639776000134)

3. Mitchell, J. J. (2019). Regional Scale Dryland Vegetation Classification with an Integrated Lidar-Hyperspectral Approach. *Remote Sensing, MDPI*.  
   [https://www.mdpi.com/2072-4292/11/18/2141/htm](https://www.mdpi.com/2072-4292/11/18/2141/htm)

4. David, H. C. (2023). Tree Species Classification in a Complex Brazilian Tropical Forest Using Hyperspectral and LiDAR Data. *Forests, MDPI*.  
   [https://www.mdpi.com/1999-4907/14/5/945](https://www.mdpi.com/1999-4907/14/5/945)

5. Sankey, T., Donager, J., Mcvay, J. (2017). UAV lidar and hyperspectral fusion for forest monitoring in the southwestern USA. *Remote Sensing of Environment*.  
   [https://www.sciencedirect.com/science/article/pii/S0034425717301578](https://www.sciencedirect.com/science/article/pii/S0034425717301578)

---
## Web Sources Used

1. [A comprehensive review of hyperspectral data fusion with lidar and sar data](https://www.sciencedirect.com/science/article/pii/S1367578821000110)
2. [Fusion of hyperspectral imaging and LiDAR for forest monitoring](https://www.sciencedirect.com/science/article/pii/B9780444639776000134)
3. [Regional Scale Dryland Vegetation Classification with an Integrated Lidar-Hyperspectral Approach](https://www.mdpi.com/2072-4292/11/18/2141/htm)
4. [Tree Species Classification in a Complex Brazilian Tropical Forest Using Hyperspectral and LiDAR Data](https://www.mdpi.com/1999-4907/14/5/945)
5. [UAV lidar and hyperspectral fusion for forest monitoring in the southwestern USA](https://www.sciencedirect.com/science/article/pii/S0034425717301578)
