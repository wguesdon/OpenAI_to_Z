# Comparison of Digital Elevation Models for the Amazon Basin

## Question
What digital elevation models (DEMs) are available covering the Amazon basin?

## Overview
Several high-quality digital elevation models (DEMs) are available that cover the Amazon basin region. This report will provide an overview and comparison of some of the key DEM datasets that are relevant for this area.

## Copernicus Digital Elevation Model (DEM)
[Copernicus DEM](https://registry.opendata.aws/copernicus-dem/) is a global digital surface model (DSM) produced by the European Union's Copernicus Earth observation program. It provides worldwide coverage at two resolutions:

- GLO-30 Public: 30-meter resolution, with some areas not yet publicly released
- GLO-90: 90-meter resolution, with full global coverage

The Copernicus DEM represents the Earth's surface including buildings, infrastructure and vegetation. It is derived from the TanDEM-X radar satellite mission.

## SRTM 90m DEM
The [SRTM 90m Digital Elevation Database](https://srtm.csi.cgiar.org/) is a widely used global DEM dataset produced from the Shuttle Radar Topography Mission (SRTM). It provides 90-meter resolution elevation data covering most of the globe between 60°N and 54°S latitude.

The SRTM data has been processed by the CGIAR-CSI to fill data voids and optimize its usability. This is considered one of the highest quality SRTM datasets available.

## NASADEM
[NASADEM](https://lpdaac.usgs.gov/products/nasadem_hgtv001/) is another global DEM dataset derived from the original SRTM data. It incorporates additional processing and improvements, including:

- Use of ICESat GLAS ground control points for better geolocation accuracy
- Conversion to a geoid reference
- Incorporation of ASTER GDEM and ALOS PRISM DEM data for void filling

NASADEM provides 1 arc-second (~30 meter) resolution elevation data globally.

## MERIT DEM
The [MERIT DEM](https://hydro.iis.u-tokyo.ac.jp/~yamadai/MERIT_DEM/list_5deg.html) is a global 3 arc-second (~90 meter) resolution digital elevation model developed by researchers at the University of Tokyo. It aims to provide an improved terrain representation by removing multiple types of error present in previous global DEMs.

The MERIT DEM is freely available for research and educational use, with some restrictions on commercial applications.

## Comparison and Recommendations
All of the DEM datasets discussed cover the Amazon basin region and provide high-quality elevation data. Some key points of comparison:

- **Resolution**: The Copernicus GLO-30 and NASADEM offer the highest spatial resolution at ~30 meters, while the SRTM 90m and MERIT DEM are at 90 meters.
- **Coverage**: The Copernicus GLO-90 and SRTM 90m have full global coverage, while the higher resolution GLO-30 and NASADEM have some gaps.
- **Accuracy**: The MERIT DEM is reported to have the most accurate terrain representation by addressing multiple error sources in previous DEMs.

For Amazon basin applications, the MERIT DEM or SRTM 90m datasets are likely the best starting points due to their pan-Amazon coverage and relatively high 90-meter resolution. The Copernicus GLO-30 or NASADEM could also be considered if the higher 30-meter resolution is required for a specific use case.

## References
[Copernicus Digital Elevation Model (DEM)](https://registry.opendata.aws/copernicus-dem/)
[CGIAR-CSI SRTM – SRTM 90m DEM Digital Elevation Database](https://srtm.csi.cgiar.org/)
[Copernicus Global Digital Elevation Models](https://portal.opentopography.org/datasetMetadata?otCollectionID=OT.032021.4326.1)
[LP DAAC - NASADEM_HGT](https://lpdaac.usgs.gov/products/nasadem_hgtv001/)
[MERIT DEM: Multi-Error-Removed Improved-Terrain DEM](https://hydro.iis.u-tokyo.ac.jp/~yamadai/MERIT_DEM/list_5deg.html)

---
## Web Sources Used

1. [Copernicus Digital Elevation Model (DEM)](https://registry.opendata.aws/copernicus-dem/)
2. [CGIAR-CSI SRTM – SRTM 90m DEM Digital Elevation Database](https://srtm.csi.cgiar.org/)
3. [Copernicus Global Digital Elevation Models](https://portal.opentopography.org/datasetMetadata?otCollectionID=OT.032021.4326.1)
4. [LP DAAC - NASADEM_HGT](https://lpdaac.usgs.gov/products/nasadem_hgtv001/)
5. [MERIT DEM: Multi-Error-Removed Improved-Terrain DEM](https://hydro.iis.u-tokyo.ac.jp/~yamadai/MERIT_DEM/list_5deg.html)
