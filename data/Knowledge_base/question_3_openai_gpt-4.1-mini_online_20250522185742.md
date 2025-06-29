# Machine Learning Models for Identifying Archaeological Features Beneath Forest Canopy

## Restatement of the Question
What machine learning models have successfully identified archaeological features beneath forest canopy?

---

## Introduction
Detecting archaeological features hidden beneath dense forest canopies is a significant challenge due to vegetation obstructing ground visibility. Advances in remote sensing, especially Light Detection and Ranging (LiDAR) technology, have enabled the acquisition of high-resolution terrain data, even under dense vegetation. The combination of LiDAR datasets and machine learning models has increasingly shown promising results in automatically identifying archaeological sites obscured by forest cover.

---

## Overview of Archaeological Feature Detection Beneath Forest Canopies

### Role of LiDAR in Archaeology
- Airborne LiDAR provides a means to "see through" woodland canopies by capturing ground elevation models with precision, allowing the detection of micro-relief features associated with archaeological remains.
- Studies demonstrate the application of LiDAR data to various forest types including Mediterranean and boreal forests, effectively revealing ancient structures such as fortresses and small-scale land use patterns previously undetectable at ground level.

### Challenges
- Dense vegetation, protected areas with restricted access, and the subtlety of ground disturbances require sophisticated data analysis techniques.
- Nationwide LiDAR datasets often vary in resolution, which can affect the accuracy of archaeological identifications.

---

## Machine Learning Approaches in Archaeological Feature Detection

### Convolutional Neural Networks (CNNs) and Deep Learning
- A significant breakthrough involves the use of **modified Mask Region-based Convolutional Neural Networks (Mask R-CNN)** on high-resolution digital elevation models (DEMs) derived from LiDAR data.
- This approach leverages image preprocessing and augmentation to enhance detection and classification of archaeological features, such as burial mounds and ancient charcoal production sites.
- Optimization techniques like AdaBound further improve model accuracy and reduce training time.
- Reported performance: 
  - Average recall of 83%
  - Average precision of 87%
- These models produce bias-free, efficient large-scale archaeological site mappings and are demonstrated successfully in landscapes such as the North German Lowland ([wiley.com](https://onlinelibrary.wiley.com/doi/10.1002/arp.1806)).

### Use of Different Resolutions of LiDAR Data
- Studies comparing **low-resolution (LR) and high-resolution (HR) airborne laser scanning (ALS) data** found that HR data allows detection of approximately three times more cultural remains.
- While this is not strictly a machine learning model, it informs model selection and data preprocessing decisions necessary for effective feature detection.
- Improvements in ground-point classification and terrain model generation enhance input data quality, crucial for any subsequent machine learning detection task ([tandfonline.com](https://www.tandfonline.com/doi/full/10.1080/00934690.2019.1677424)).

---

## Summary of Key Findings

| Model/Technique                          | Data Source            | Feature Type                      | Performance/Outcome                         | References                         |
|----------------------------------------|-----------------------|---------------------------------|--------------------------------------------|----------------------------------|
| Modified Mask R-CNN + AdaBound          | High-resolution LiDAR DEMs | Archaeological sites (e.g., RCH sites)  | Recall: 83%, Precision: 87%, time-efficient | [wiley.com](https://onlinelibrary.wiley.com/doi/10.1002/arp.1806) |
| High-Resolution vs Low-Resolution ALS Data | Airborne Laser Scanning | Cultural remains in boreal forests | HR data detects ~3x more remains          | [tandfonline.com](https://www.tandfonline.com/doi/full/10.1080/00934690.2019.1677424) |

---

## Conclusion
Machine learning models, particularly **deep learning frameworks like modified Mask R-CNN**, have shown strong success in automatically detecting archaeological features beneath forest canopies when paired with high-resolution LiDAR-derived terrain models. These techniques yield high accuracy and efficiency, significantly aiding archaeological prospection in vegetated and challenging environments.

---

## References

- Bonhage, A., Eltaher, M., Raab, T., Breuß, M., Raab, A., & Schneider, A. "A modified Mask region‐based convolutional neural network approach for the automated detection of archaeological sites on high‐resolution light detection and ranging‐derived digital elevation models in the North German Lowland." *Archaeological Prospection*, 2021. [wiley.com](https://onlinelibrary.wiley.com/doi/10.1002/arp.1806)

- Norstedt, G., Axelsson, A.-L., Laudon, H., Östlund, L. "Detecting Cultural Remains in Boreal Forests in Sweden Using Airborne Laser Scanning Data of Different Resolutions." *Journal of Field Archaeology*, 2019. [tandfonline.com](https://www.tandfonline.com/doi/full/10.1080/00934690.2019.1677424)

- Domínguez-Jiménez, J. L. "Revealing Archaeological Sites under Mediterranean Forest Canopy Using LiDAR: El Viandar Castle (husum) in El Hoyo (Belmez-Córdoba, Spain)." *Drones*, 2021. [mdpi.com](https://www.mdpi.com/2504-446X/5/3/72)

- Devereux, B. J., Amable, G. S., Crow, P., Cliff, A. D. "The potential of airborne lidar for detection of archaeological features under woodland canopies." *Antiquity*. [cambridge.org](https://www.cambridge.org/core/journals/antiquity/article/potential-of-airborne-lidar-for-detection-of-archaeological-features-under-woodland-canopies/6224202F4EF4CE1C80924904B84B180B)

- Doneus, M., Briese, C., Fera, M., Janner, M. "Archaeological prospection of forested areas using full-waveform airborne laser scanning." *Journal of Archaeological Science*, 2008. [sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0305440307001252)

---
## Web Sources Used

1. [The potential of airborne lidar for detection of archaeological features under woodland canopies](https://www.cambridge.org/core/journals/antiquity/article/potential-of-airborne-lidar-for-detection-of-archaeological-features-under-woodland-canopies/6224202F4EF4CE1C80924904B84B180B)
2. [Archaeological prospection of forested areas using full-waveform airborne laser scanning](https://www.sciencedirect.com/science/article/pii/S0305440307001252)
3. [Revealing Archaeological Sites under Mediterranean Forest Canopy Using LiDAR: El Viandar Castle (husum) in El Hoyo (Belmez-Córdoba, Spain)](https://www.mdpi.com/2504-446X/5/3/72)
4. [Detecting Cultural Remains in Boreal Forests in Sweden Using Airborne Laser Scanning Data of Different Resolutions](https://www.tandfonline.com/doi/full/10.1080/00934690.2019.1677424)
5. [A modified Mask region‐based convolutional neural network approach for the automated detection of archaeological sites on high‐resolution light detection and ranging‐derived digital elevation models in the North German Lowland](https://onlinelibrary.wiley.com/doi/10.1002/arp.1806)
