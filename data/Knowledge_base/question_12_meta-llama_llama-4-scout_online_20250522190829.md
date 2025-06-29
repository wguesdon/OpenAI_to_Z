# Digital Elevation Models (DEMs) Covering the Amazon Basin
The Amazon basin, being the largest river basin in the world, covering an area of over 7 million square kilometers across nine countries in South America, presents a significant interest for various studies including hydrology, ecology, and geology. Several digital elevation models (DEMs) are available that cover this vast region, each with its own characteristics, advantages, and limitations.

## Available DEMs

### 1. Copernicus Digital Elevation Model (DEM)
The Copernicus DEM is a Digital Surface Model (DSM) representing the Earth's surface, including buildings, infrastructure, and vegetation. It offers two instances: GLO-30 Public and GLO-90, providing worldwide coverage at 30 meters and 90 meters resolution, respectively. However, the availability of GLO-30 data is limited for certain countries. Ocean areas are not covered, with assumed height values equal to zero [registry.opendata.aws](https://registry.opendata.aws/copernicus-dem/).

### 2. SRTM 90m DEM Digital Elevation Database
The CGIAR-CSI SRTM 90m DEM is a widely used dataset that provides digital elevation data for the entire world. This dataset was originally produced by NASA and has been processed to fill data voids and facilitate ease of use. It's particularly noted for its high quality and availability for large portions of the tropics and other areas [srtm.csi.cgiar.org](https://srtm.csi.cgiar.org/).

### 3. Copernicus Global Digital Elevation Models
This DSM is derived from an edited DSM named WorldDEM, with specific editing for water bodies, shore- and coastlines, and terrain structures. The data is available through OpenTopography, providing access to the global GLO-30 and GLO-90 Defence Gridded Elevation Data (DGED) [portal.opentopography.org](https://portal.opentopography.org/datasetMetadata?otCollectionID=OT.032021.4326.1).

### 4. NASADEM_HGT
NASADEM data products were derived from the Shuttle Radar Topography Mission (SRTM) and additional sources like ASTER GDEM Version 2 and ICESat GLAS ground control points. These improvements aim at enhancing surface elevation measurements and geolocation accuracy [lpdaac.usgs.gov](https://lpdaac.usgs.gov/products/nasadem_hgtv001/).

### 5. MERIT DEM: Multi-Error-Removed Improved-Terrain DEM
The MERIT DEM is another dataset that has been specifically designed to minimize errors present in existing DEMs, improving terrain representation. It's freely available for research and education purposes, with certain conditions for commercial use [hydro.iis.u-tokyo.ac.jp](https://hydro.iis.u-tokyo.ac.jp/~yamadai/MERIT_DEM/list_5deg.html).

## Comparison and Suitability
- **Resolution and Accuracy**: SRTM and MERIT DEMs offer resolutions of 90 meters and 3 arcseconds (~90 meters at the equator), respectively. Copernicus DEM provides 30 and 90 meters resolutions.
- **Coverage**: Most of these DEMs offer global coverage, but the availability of high-resolution data like GLO-30 might be limited in certain regions.
- **Application**: The choice of DEM depends on the specific application, such as hydrological modeling, geological studies, or environmental assessments.

## Conclusion
Several digital elevation models are available that cover the Amazon basin, each with its strengths and limitations. The choice of DEM should be based on the specific requirements of the project, including resolution, accuracy, and the intended application.

## References
- [registry.opendata.aws](https://registry.opendata.aws/copernicus-dem/)
- [srtm.csi.cgiar.org](https://srtm.csi.cgiar.org/)
- [portal.opentopography.org](https://portal.opentopography.org/datasetMetadata?otCollectionID=OT.032021.4326.1)
- [lpdaac.usgs.gov](https://lpdaac.usgs.gov/products/nasadem_hgtv001/)
- [hydro.iis.u-tokyo.ac.jp](https://hydro.iis.u-tokyo.ac.jp/~yamadai/MERIT_DEM/list_5deg.html)

---
## Web Sources Used

1. [Copernicus Digital Elevation Model (DEM)](https://registry.opendata.aws/copernicus-dem/)
2. [CGIAR-CSI SRTM – SRTM 90m DEM Digital Elevation Database](https://srtm.csi.cgiar.org/)
3. [Copernicus Global Digital Elevation Models](https://portal.opentopography.org/datasetMetadata?otCollectionID=OT.032021.4326.1)
4. [LP DAAC - NASADEM_HGT](https://lpdaac.usgs.gov/products/nasadem_hgtv001/)
5. [MERIT DEM: Multi-Error-Removed Improved-Terrain DEM](https://hydro.iis.u-tokyo.ac.jp/~yamadai/MERIT_DEM/list_5deg.html)
