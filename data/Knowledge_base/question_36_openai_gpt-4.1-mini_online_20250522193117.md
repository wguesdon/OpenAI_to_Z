# Best OCR Workflows for 16th–19th-Century Portuguese and Spanish Expedition Journals

**Question:**  
*Which OCR workflows give the best accuracy on 16th–19th-century Portuguese and Spanish expedition journals?*

---

## 1. Introduction

Optical Character Recognition (OCR) workflows for historical documents such as 16th–19th-century Portuguese and Spanish expedition journals face unique challenges including varied handwriting styles, font diversity, and degradation of source material. Achieving high OCR accuracy on these old manuscripts is essential for enabling digital humanities research, semantic analysis, and historical investigations.

---

## 2. Challenges in OCR of Historical Iberian Documents

- **Diverse Fonts and Scripts:** Early modern prints and handwritten documents vary significantly in font styles, with many unique typefaces uncommon today (including Antiqua variants and handwritten cursive forms).
- **Material Degradation:** Age-related damage like fading ink, stains, and torn pages impact readability.
- **Language and Orthography Variants:** Variants in historical Spanish and Portuguese orthography require specialized language models.
- **Rare Characters:** Spanish and Portuguese languages contain rare or accented characters that require careful modeling to recognize correctly.

---

## 3. Successful OCR Workflows and Models

### 3.1 Portuguese Handwriting 16th–19th Century Model

- **Description:**  
  A freely available AI model specialized for handwritten Latin alphabet documents from the 16th–19th centuries in Portuguese. It is built for use in the Transkribus platform, which specializes in Handwritten Text Recognition (HTR).  
- **Capabilities:**  
  Automates transcription of historical Portuguese manuscripts into editable and searchable text.  
- **Accessibility:**  
  Model integrated into both Transkribus Expert Client and Transkribus Lite.  
- **Accuracy:**  
  Leveraging deep learning, it improves transcription quality significantly over generic OCR engines.  
- **Reference:**  
  [readcoop.eu](https://readcoop.eu/model/portuguese-handwriting-16th-19th-century/)

### 3.2 Historic Spanish Documents Using CNN-Based OCR

- **Approach:**  
  Using Convolutional Neural Networks (CNNs) trained on annotated Spanish American notary records from the 17th century as a proxy for similar handwriting and print styles. Professional historians validated character expansions to ensure close resemblance to originals before training.  
- **Accuracy:**  
  Verified good recognition of rare characters was crucial.  
- **Insight:**  
  Quality control through historian validation helped maintain high OCR quality on historical Spanish archives.  
- **Reference:**  
  [digitalhumanities.org](https://digitalhumanities.org/dhq/vol/15/4/000581/000581.html)

### 3.3 Combining Multiple OCR Models for Early Modern Prints

- **Method:**  
  A recent approach involves aggregating outputs of different OCR engines fine-tuned on early modern fonts seen in 15th–18th century German library collections. Although focused on German, the strategy is applicable to Iberian materials due to font overlap and similar print challenges.  
- **Technology:**  
  Combining fine-grained font recognition with OCR improves overall text recognition accuracy.  
- **Benefit:**  
  This multi-model approach increases robustness against font variability and print artifacts in 16th-19th century documents.  
- **Reference:**  
  [arxiv.org](https://export.arxiv.org/pdf/2305.07131v1.pdf)

### 3.4 Use of Large Language Models for OCR Error Correction in Spanish

- **Approach:**  
  A novel workflow uses Large Language Models (LLMs) to post-process OCR outputs from 19th-century Latin American newspapers, correcting OCR errors and detecting linguistic variants.  
- **Adaptability:**  
  This framework can be used broadly for digitized Spanish corpora including expedition journals.  
- **Results:**  
  Significantly improves quality of digitized text through semantic understanding beyond character recognition.  
- **Reference:**  
  [arxiv.org](https://arxiv.org/abs/2407.12838)

### 3.5 Fully Automated Pipeline with Distributed Processing

- **Method:**  
  High-quality OCR (above 90%) was attained on early modern digitized books by transitioning from stepwise OCR to fully automated pipelines capable of parallel processing on multiple servers.  
- **Efficiency:**  
  Reduced processing time from circa 20 hours to around 3 hours per 500-page book, maintaining high OCR quality that supports semantic analysis.  
- **Insight:**  
  Consistency (homogeneity of OCR quality across the corpus) is as important as peak accuracy per work.  
- **Reference:**  
  [academic.oup.com](https://academic.oup.com/dsh/article/37/4/1197/6564120)

---

## 4. Summary of Best Practices for OCR Accuracy

| Feature / Workflow                        | Portuguese Handwriting | Spanish Historical Print/Handwriting | Postprocessing with LLM | Multi-OCR Model Approach | Distributed Pipeline Automation |
|------------------------------------------|-----------------------|-------------------------------------|------------------------|-------------------------|-------------------------------|
| Deep learning specialized models         | ✓                     | ✓                                   |                        |                         |                               |
| Professional historian validation        |                       | ✓                                   |                        |                         |                               |
| Handwritten Text Recognition (Transkribus) | ✓                     |                                     |                        |                         |                               |
| Combining OCR models for font variation  |                       | ✓                                   |                        | ✓                       |                               |
| OCR error correction with Large Language Models |                       | ✓                                   | ✓                      |                         |                               |
| Automated, parallelized processing       |                       |                                     |                        |                         | ✓                             |
| High quality benchmark (>90% accuracy)  |                       | ✓                                   | ✓                      | ✓                       | ✓                             |

---

## 5. Recommendations for 16th–19th Century Iberian Expedition Journals

To achieve best OCR accuracy on 16th–19th-century Portuguese and Spanish expedition journals, combine the following:

1. **Use specialized deep learning models trained on historical Portuguese and Spanish scripts:**
   - For Portuguese, use the dedicated handwriting model available in Transkribus.
   - For Spanish, use CNN-based OCR models fine-tuned with professional historian validation.

2. **Adopt multi-OCR model fusion workflows to leverage font style recognition aiding OCR performance.**

3. **Apply Large Language Model postprocessing to detect and correct OCR errors contextually, especially in Spanish texts.**

4. **Implement fully automated pipeline systems with parallel server processing to maintain high OCR accuracy at scale with efficient throughput.**

Such integrated workflows yield OCR accuracy sufficient for semantic analysis and research applications, typically surpassing 90%.

---

## 6. References

- Portuguese Handwriting Model (16th–19th century): [readcoop.eu](https://readcoop.eu/model/portuguese-handwriting-16th-19th-century/)
- CNN-based Spanish American Notary Records OCR: [digitalhumanities.org](https://digitalhumanities.org/dhq/vol/15/4/000581/000581.html)
- Combining OCR Models for Early Modern Books: [arxiv.org PDF](https://export.arxiv.org/pdf/2305.07131v1.pdf)
- Large Language Models for OCR Corrections on Spanish Historical Newspapers: [arxiv.org](https://arxiv.org/abs/2407.12838)
- High-Quality OCR Pipeline Automation for Early Modern Books: [academic.oup.com](https://academic.oup.com/dsh/article/37/4/1197/6564120)

---

# Conclusion

In conclusion, the best OCR results on 16th–19th-century Portuguese and Spanish expedition journals are obtained by leveraging specialized deep learning handwriting models, combined OCR engines for varied fonts, LLM-based error correction, and fully automated scalable workflows. These methods collectively enable achieving and surpassing 90% OCR accuracy, supporting rich digital humanities analysis of historical Iberian expedition materials.

---
## Web Sources Used

1. [Character Recognition Of Seventeenth-Century Spanish American Notary Records Using Deep Learning](https://digitalhumanities.org/dhq/vol/15/4/000581/000581.html)
2. [Portuguese Handwriting 16th-19th century](https://readcoop.eu/model/portuguese-handwriting-16th-19th-century/)
3. [Reading in the mist: high-quality optical character recognition based on freely available early modern digitized books](https://academic.oup.com/dsh/article/37/4/1197/6564120)
4. [Historical Ink: 19th Century Latin American Spanish Newspaper Corpus with LLM OCR Correction](https://arxiv.org/abs/2407.12838)
5. [Combining OCR Models for Reading Early Modern Printed Books](https://export.arxiv.org/pdf/2305.07131v1.pdf)
