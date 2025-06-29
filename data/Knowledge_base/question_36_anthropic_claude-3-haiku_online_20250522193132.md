# Optimizing OCR Workflows for 16th–19th-century Portuguese and Spanish Expedition Journals

## Question Restatement

Which OCR workflows give the best accuracy on 16th–19th-century Portuguese and Spanish expedition journals?

## Introduction

Historical handwritten documents, such as expedition journals from the 16th-19th centuries, pose unique challenges for optical character recognition (OCR) due to the varied writing styles, languages, and quality of the source material. Accurate transcription of these important documents is crucial for enabling digital access and analysis. This report examines the current state of OCR technology and workflows that can be leveraged to achieve high accuracy on Portuguese and Spanish expedition journals from this time period.

## Approaches to High-Accuracy OCR for Historical Documents

### 1. Leveraging Pre-Trained Models
[readcoop.eu](https://readcoop.eu/model/portuguese-handwriting-16th-19th-century/) provides a pre-trained Handwritten Text Recognition (HTR) model for 16th-19th century Portuguese handwriting, which can be used in the Transkribus platform to automatically transcribe documents. This model was trained on a large corpus of historical documents and can provide a strong starting point for processing expedition journals.

Similarly, [digitalhumanities.org](https://digitalhumanities.org/dhq/vol/15/4/000581/000581.html) describes the development of a deep learning-based OCR model for 17th-century Spanish American notary records, which could be adapted for expedition journals in Spanish.

### 2. Corpus-Specific Model Training
[academic.oup.com](https://academic.oup.com/dsh/article/37/4/1197/6564120) highlights the importance of training OCR models on a corpus-specific dataset to achieve high accuracy, even on historical documents. This may involve creating a labeled dataset of expedition journal pages and fine-tuning a pre-trained model or training a custom model from scratch.

### 3. Leveraging Large Language Models for Error Correction
[arxiv.org](https://arxiv.org/abs/2407.12838) introduces a framework for using large language models (LLMs) to correct OCR errors in digitized historical corpora, including 19th-century Latin American newspapers. This approach could be extended to expedition journals, where the LLM could learn the linguistic patterns and surface forms specific to these documents.

### 4. Combining Multiple OCR Models
[arxiv.org](https://export.arxiv.org/pdf/2305.07131v1.pdf) explores the idea of combining multiple OCR models to improve accuracy on early modern printed books, which share some similarities with handwritten expedition journals. By using ensemble methods or other techniques to leverage the complementary strengths of different models, it may be possible to achieve higher accuracy than any single model.

## Recommendations

Based on the reviewed literature, the following recommendations can be made for optimizing OCR workflows for 16th–19th-century Portuguese and Spanish expedition journals:

1. **Utilize Pre-Trained Models**: Start with the available pre-trained models, such as the Portuguese HTR model from [readcoop.eu](https://readcoop.eu/model/portuguese-handwriting-16th-19th-century/) and the Spanish notary records model from [digitalhumanities.org](https://digitalhumanities.org/dhq/vol/15/4/000581/000581.html), and fine-tune them on a corpus-specific dataset of expedition journals.

2. **Create Corpus-Specific Training Data**: Invest in the creation of a labeled dataset of expedition journal pages, representing the diverse writing styles, languages, and document qualities present in the corpus. Use this dataset to train custom OCR models or fine-tune pre-trained models.

3. **Incorporate Large Language Model-based Error Correction**: Explore the framework described in [arxiv.org](https://arxiv.org/abs/2407.12838) to leverage large language models for correcting OCR errors in the expedition journal texts, further improving the overall accuracy.

4. **Combine Multiple OCR Models**: Experiment with ensemble methods or other techniques to combine the outputs of different OCR models, as suggested in [arxiv.org](https://export.arxiv.org/pdf/2305.07131v1.pdf), to leverage the complementary strengths of the models and achieve higher accuracy.

By implementing these recommendations, researchers and archivists can optimize their OCR workflows to produce high-quality, accurate transcriptions of 16th–19th-century Portuguese and Spanish expedition journals, enabling improved digital access and analysis of these valuable historical documents.

## References

[readcoop.eu](https://readcoop.eu/model/portuguese-handwriting-16th-19th-century/)
[digitalhumanities.org](https://digitalhumanities.org/dhq/vol/15/4/000581/000581.html)
[academic.oup.com](https://academic.oup.com/dsh/article/37/4/1197/6564120)
[arxiv.org](https://arxiv.org/abs/2407.12838)
[arxiv.org](https://export.arxiv.org/pdf/2305.07131v1.pdf)

---
## Web Sources Used

1. [Portuguese Handwriting 16th-19th century](https://readcoop.eu/model/portuguese-handwriting-16th-19th-century/)
2. [Character Recognition Of Seventeenth-Century Spanish American Notary Records Using Deep Learning](https://digitalhumanities.org/dhq/vol/15/4/000581/000581.html)
3. [Reading in the mist: high-quality optical character recognition based on freely available early modern digitized books](https://academic.oup.com/dsh/article/37/4/1197/6564120)
4. [Historical Ink: 19th Century Latin American Spanish Newspaper Corpus with LLM OCR Correction](https://arxiv.org/abs/2407.12838)
5. [Combining OCR Models for Reading Early Modern Printed Books](https://export.arxiv.org/pdf/2305.07131v1.pdf)
