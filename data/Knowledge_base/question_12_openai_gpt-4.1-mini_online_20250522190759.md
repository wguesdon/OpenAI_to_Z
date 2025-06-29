# Available Digital Elevation Models (DEMs) Covering the Amazon Basin

**Question:**  
*What digital elevation models (DEMs) are available covering the Amazon basin?*

---

## Overview

The Amazon basin, spanning multiple South American countries and a vast expanse, is covered by several prominent Digital Elevation Models (DEMs) that provide varying resolutions, coverages, and data qualities. These DEMs have been produced using different sensor technologies such as radar interferometry and lidar, and they are accessible for research and some for commercial use.

---

## Summary of DEMs Covering the Amazon Basin

### 1. Copernicus Digital Elevation Model (DEM)
- **Coverage:** Worldwide, including the Amazon basin; provides two instances:
  - **GLO-90:** Global coverage at 90-meter resolution.
  - **GLO-30 Public:** Limited worldwide coverage at 30-meter resolution; a subset of tiles covering specific countries may still be restricted.
- **Type:** Digital Surface Model (DSM), including buildings, infrastructure, and vegetation.
- **Special Notes:** Water bodies are not given height tiles; ocean areas assume height zero.
- **Access:** Public datasets available via ESA and OpenTopography portal.
- **Source:** Copernicus DEM is derived from the radar satellite data acquired during the TanDEM-X mission, edited for features like water bodies and airports.
- **Link:** [registry.opendata.aws](https://registry.opendata.aws/copernicus-dem/), [opentopography.org](https://portal.opentopography.org/datasetMetadata?otCollectionID=OT.032021.4326.1)

### 2. CGIAR-CSI Shuttle Radar Topography Mission (SRTM) 90m DEM
- **Coverage:** Global, including the entire Amazon basin.
- **Resolution:** 90 meters.
- **Type:** Elevation data from radar interferometry collected by NASA's SRTM mission.
- **Key Features:** Processed to fill data gaps and voids; considered one of the highest quality SRTM datasets.
- **Use Cases:** Ideal for broad-scale studies requiring moderate resolution elevation data.
- **Link:** [srtm.csi.cgiar.org](https://srtm.csi.cgiar.org/)

### 3. NASADEM
- **Coverage:** Global, including the Amazon basin.
- **Resolution:** Comparable to SRTM 30m and 90m datasets.
- **Source:** An enhanced reprocessing of SRTM data, incorporating additional data from ICESat's lidar (GLAS), ASTER GDEM, and PRISM AW3D30 to improve elevation and geolocation accuracy.
- **Improvements:** Void filling, geoid references, and more accurate surface height.
- **Use Cases:** Advanced terrain representation suitable for researchers needing higher accuracy than original SRTM.
- **Link:** [lpdaac.usgs.gov](https://lpdaac.usgs.gov/products/nasadem_hgtv001/)

### 4. MERIT DEM (Multi-Error-Removed Improved-Terrain DEM)
- **Coverage:** Global, including the Amazon basin.
- **Resolution:** Approximately 90 meters.
- **Key Feature:** Error-corrected and processed to remove systematic errors such as radar-related biases and vegetation effects present in other datasets.
- **Access:** Freely available for research and educational purposes, with certain conditions on commercial use.
- **Use Cases:** Enhanced elevation data quality for hydrological and geomorphological studies.
- **Link:** [hydro.iis.u-tokyo.ac.jp](https://hydro.iis.u-tokyo.ac.jp/~yamadai/MERIT_DEM/list_5deg.html)

---

## Considerations for Amazon Basin DEM Selection

- **Resolution:** DEMs range mostly between 30m (GLO-30 Public Copernicus DEM, NASADEM) and 90m (CGIAR-CSI SRTM, Copernicus GLO-90, MERIT DEM).
- **Surface Type:** DSMs like Copernicus include surface features (trees, buildings), while others aim to model bare earth elevation.
- **Data Voids & Corrections:** Some products such as MERIT and NASADEM focus on filling data gaps and correcting systematic errors, which is particularly valuable in densely forested areas like the Amazon.
- **Access & Usage:** Most DEMs are freely available for research; however, commercial use may require permissions (e.g., MERIT DEM).

---

## Conclusion

The Amazon basin is well-covered by several global digital elevation models, each offering different strengths in spatial resolution, accuracy, and surface representation:

| DEM Product                     | Resolution  | Coverage             | Type            | Notes                          |
|--------------------------------|-------------|----------------------|-----------------|-------------------------------|
| Copernicus DEM (GLO-30, GLO-90) | 30m / 90m   | Global (limited GLO-30) | DSM             | Includes surface features; detailed editing applied. |
| CGIAR-CSI SRTM 90m             | 90m         | Global               | DEM             | Widely used, good quality for tropics. |
| NASADEM                        | ~30m / 90m  | Global               | DEM             | Enhanced SRTM with lidar corrections. |
| MERIT DEM                      | ~90m        | Global               | DEM             | Systematic error removed; improved for hydrology and forested regions. |

For detailed applications in the Amazon basin, researchers often combine these DEMs considering their specific requirements for resolution and accuracy.

---

## References

- Copernicus Digital Elevation Model (DEM), Global Coverage  
  https://registry.opendata.aws/copernicus-dem/  
  https://portal.opentopography.org/datasetMetadata?otCollectionID=OT.032021.4326.1

- CGIAR-CSI SRTM 90m Digital Elevation Database  
  https://srtm.csi.cgiar.org/

- NASADEM Data Products (Enhanced SRTM)  
  https://lpdaac.usgs.gov/products/nasadem_hgtv001/

- MERIT DEM: Multi-Error-Removed Improved-Terrain DEM  
  https://hydro.iis.u-tokyo.ac.jp/~yamadai/MERIT_DEM/list_5deg.html

---

This information can assist in selecting the appropriate DEM product for geographic, hydrologic, or environmental studies within the Amazon basin.

---
## Web Sources Used

1. [Copernicus Digital Elevation Model (DEM)](https://registry.opendata.aws/copernicus-dem/)
2. [CGIAR-CSI SRTM – SRTM 90m DEM Digital Elevation Database](https://srtm.csi.cgiar.org/)
3. [Copernicus Global Digital Elevation Models](https://portal.opentopography.org/datasetMetadata?otCollectionID=OT.032021.4326.1)
4. [LP DAAC - NASADEM_HGT](https://lpdaac.usgs.gov/products/nasadem_hgtv001/)
5. [MERIT DEM: Multi-Error-Removed Improved-Terrain DEM](https://hydro.iis.u-tokyo.ac.jp/~yamadai/MERIT_DEM/list_5deg.html)
