\# AI-Powered Job Market Intelligence System



\## Project Overview

The AI-Powered Job Market Intelligence System is a machine learning-based project designed to analyze job market data and predict job role categories using Natural Language Processing (NLP).



The system helps users understand job market trends and classify job descriptions into relevant role families.



\## Objectives

\- Analyze job market data using Exploratory Data Analysis (EDA).

\- Clean and preprocess job descriptions.

\- Apply NLP techniques for text processing.

\- Train and evaluate machine learning classification models.

\- Build an interactive dashboard using Streamlit.



\## Technologies Used

\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- NLTK

\- Scikit-learn

\- TF-IDF

\- Streamlit

\- Jupyter Notebook

\- Git \& GitHub



\## Machine Learning Models

The following classification models were evaluated:



| Model | Accuracy |

|---|---:|

| Logistic Regression | 61.01% |

| Multinomial Naive Bayes | 12.53% |

| Linear SVC | 68.48% |



\*\*Best-performing model:\*\* Linear Support Vector Classifier (Linear SVC).



\## Streamlit Dashboard

The interactive dashboard includes:

\- Job Market Dashboard

\- Job Role Prediction

\- Model Performance

\- About Project



\## Project Structure

```text

AI JOB SIMULATION/

│

├── NOTES.md/

│   ├── day2\_eda.ipynb

│   ├── ml\_model.ipynb

│   └── notes.md

│

├── app.py

├── requirements.txt

├── README.md

├── .gitignore

│

├── datasets/       (local data files)

└── models/         (trained model files)

```



\## How to Run the Project



1\. Clone the repository:

```bash

git clone https://github.com/adila1016/AI-Job-Market-Intelligence-System.git

```



2\. Navigate to the project folder:

```bash

cd AI-Job-Market-Intelligence-System

```



3\. Install dependencies:

```bash

pip install -r requirements.txt

```



4\. Run the Streamlit application:

```bash

streamlit run app.py

```



\## Future Improvements

\- Improve classification performance.

\- Expand job market analysis.

\- Add FastAPI integration.

\- Deploy the application using AWS.



\## Author

Adila Fathima



GitHub: https://github.com/adila1016



