## Overview
This Jupyter notebook implements a Natural Language Processing (NLP) classification project for spam detection in SMS messages. It is part of Deep Learning Lab Assignment 4.

**Author:** Chetanraje Gund  
**PRN:** 202301040080  
**Batch:** PEC1  
**Branch:** Computer Engineering  
**Subject:** Deep Learning Lab  

## Features
- **Data Preprocessing:** Tokenization, stopword removal, stemming, and lemmatization using NLTK
- **Text Vectorization:** Implementation of both TF-IDF and Count Vectorization techniques
- **Classification Models:** Multinomial Naive Bayes and Logistic Regression classifiers
- **Model Evaluation:** Comprehensive metrics including accuracy, precision, recall, F1-score, and confusion matrices
- **Visualization:** Performance comparison and analysis plots

## Dependencies
The notebook requires the following Python libraries:
- pandas
- numpy
- scikit-learn
- nltk
- matplotlib
- seaborn (if used for plots)

Install dependencies using:
```bash
pip install pandas numpy scikit-learn nltk matplotlib seaborn
```

Additionally, download NLTK data:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

## Usage
1. Open the notebook `P4_NLP_Classification.ipynb` in Jupyter Notebook or JupyterLab.
2. Ensure all dependencies are installed.
3. Run the cells in order to execute the analysis.
4. The notebook includes data loading, preprocessing, model training, evaluation, and visualization.

## Key Findings
- Both Naive Bayes and Logistic Regression models achieved good performance on the spam classification task.
- TF-IDF vectorization was effective for text classification.
- Models were validated on new sample messages.

## Structure
- Data exploration and preprocessing
- Feature extraction using vectorizers
- Model training and hyperparameter tuning
- Performance evaluation and comparison
- Practical testing on new data

## Results
The notebook provides detailed classification reports and confusion matrices for both models, allowing for comparison of their effectiveness in spam detection.
