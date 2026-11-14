
import streamlit as st
import joblib
import re
import nltk
import pandas as pd

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# --------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="AI Job Market Intelligence",
    page_icon="💼",
    layout="wide"
)

# --------------------------------
# 2. CUSTOM CSS
# --------------------------------

st.markdown("""
<style>
.main {
    background-color: #0e1117;
}

[data-testid="stMetric"] {
    background-color: #1e2533;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #30394a;
}

.stButton > button {
    background-color: #3867d6;
    color: white;
    border-radius: 8px;
    height: 45px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #254da8;
    color: white;
}

.result-card {
    background-color: #173d32;
    padding: 25px;
    border-radius: 12px;
    border-left: 5px solid #2ecc71;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------
# 3. LOAD TRAINED MODEL
# --------------------------------

@st.cache_resource
def load_model():

    model = joblib.load(
        "models/role_family_svm.pkl"
    )

    vectorizer = joblib.load(
        "models/tfidf_vectorizer.pkl"
    )

    return model, vectorizer


try:
    model, tfidf = load_model()

except Exception as e:
    st.error(f"Unable to load model: {e}")
    st.stop()


# --------------------------------
# 4. TEXT PREPROCESSING
# --------------------------------

@st.cache_resource
def load_nlp_resources():

    stop_words = set(stopwords.words("english"))

    lemmatizer = WordNetLemmatizer()

    return stop_words, lemmatizer


try:
    stop_words, lemmatizer = load_nlp_resources()

except LookupError:
    st.error(
        "NLTK resources are missing. "
        "Please download stopwords and wordnet."
    )
    st.stop()


def preprocess_text(text):

    text = text.lower()

    text = re.sub(
        r'[^a-zA-Z0-9\s]',
        '',
        text
    )

    tokens = text.split()

    filtered_tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    lemmatized_tokens = [
        lemmatizer.lemmatize(word)
        for word in filtered_tokens
    ]

    return " ".join(lemmatized_tokens)


# --------------------------------
# 5. SIDEBAR
# --------------------------------

st.sidebar.title("💼 AI Job Intelligence")

st.sidebar.write(
    "Machine Learning Based Job Classification"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Job Role Prediction",
        "Model Performance",
        "About Project"
    ]
)

st.sidebar.divider()

st.sidebar.info(
    "Developed using Python, NLP, "
    "TF-IDF and Machine Learning."
)


# --------------------------------
# 6. DASHBOARD PAGE
# --------------------------------

if page == "Dashboard":

    st.title(
        "💼 AI-Powered Job Market Intelligence System"
    )

    st.write(
        "Explore job market data and predict "
        "job role families using Machine Learning."
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Job Records",
        "2,471"
    )

    col2.metric(
        "Role Families",
        "15"
    )

    col3.metric(
        "Best Model",
        "Linear SVM"
    )

    col4.metric(
        "Model Accuracy",
        "68.48%"
    )

    st.divider()

    st.subheader("Job Role Distribution")

    role_data = {
        "Role": [
            "Fullstack", "Data", "Backend",
            "Operations", "Product", "Marketing",
            "HR", "Frontend", "Finance", "DevOps",
            "Sales", "Non-tech", "Customer Success",
            "Legal", "Mobile"
        ],

        "Jobs": [
            310, 240, 231, 194, 187,
            181, 166, 162, 159, 139,
            135, 128, 89, 76, 74
        ]
    }

    role_df = pd.DataFrame(role_data)

    st.bar_chart(
        role_df.set_index("Role")
    )

    st.caption(
        "Distribution of 2,471 job records "
        "across 15 role families."
    )


# --------------------------------
# 7. JOB ROLE PREDICTION PAGE
# --------------------------------

elif page == "Job Role Prediction":

    st.title("🔍 Job Role Prediction")

    st.write(
        "Enter a job title and description "
        "to predict its role family."
    )

    st.divider()

    job_title = st.text_input(
        "Enter Job Title",
        placeholder="Example: Data Scientist"
    )

    job_description = st.text_area(
        "Enter Job Description",
        placeholder="Paste the complete job description...",
        height=250
    )

    if st.button(
        "🚀 Predict Job Role",
        use_container_width=True
    ):

        if not job_title.strip() or not job_description.strip():

            st.warning(
                "Please enter both job title and job description."
            )

        else:

            original_text = (
                job_title + " " + job_description
            )

            cleaned_text = preprocess_text(
                original_text
            )

            if not cleaned_text.strip():

                st.warning(
                    "Please enter meaningful job description text."
                )

            else:

                text_vector = tfidf.transform(
                    [cleaned_text]
                )

                prediction = model.predict(
                    text_vector
                )[0]

                st.success(
                    "Job role prediction completed!"
                )

                st.markdown(
                    f"""
                    <div class="result-card">
                        <h3>Predicted Role Family</h3>
                        <h1>{prediction.replace('_', ' ').title()}</h1>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.write("")

                st.subheader("Job Description Analysis")

                word_count = len(
                    job_description.split()
                )

                char_count = len(
                    job_description
                )

                c1, c2 = st.columns(2)

                c1.metric(
                    "Word Count",
                    word_count
                )

                c2.metric(
                    "Character Count",
                    char_count
                )

                st.info(
                    "Prediction is based on the "
                    "trained Linear SVM classification model."
                )


# --------------------------------
# 8. MODEL PERFORMANCE PAGE
# --------------------------------

elif page == "Model Performance":

    st.title("📊 Model Performance")

    st.write(
        "Comparison of three machine learning classifiers."
    )

    st.divider()

    performance_data = {
        "Model": [
            "Logistic Regression",
            "Naive Bayes",
            "Linear SVM"
        ],

        "Accuracy": [
            61.01,
            12.53,
            68.48
        ],

        "Macro F1": [
            0.60,
            0.01,
            0.66
        ],

        "Weighted F1": [
            0.58,
            0.03,
            0.67
        ]
    }

    performance_df = pd.DataFrame(
        performance_data
    )

    st.dataframe(
        performance_df,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Accuracy Comparison")

    chart_df = performance_df[
        ["Model", "Accuracy"]
    ].set_index("Model")

    st.bar_chart(chart_df)

    st.success(
        "Linear SVM achieved the highest accuracy: 68.48%"
    )

    st.warning(
        "Evaluation scores measure agreement with "
        "the existing role_family_hint labels. "
        "These labels contain some noise."
    )


# --------------------------------
# 9. ABOUT PROJECT PAGE
# --------------------------------

elif page == "About Project":

    st.title("📌 About the Project")

    st.write("""
    The AI-Powered Job Market Intelligence System
    is a machine learning project designed to
    classify job descriptions into different
    professional role families.
    """)

    st.subheader("Technologies Used")

    technologies = [
        "Python",
        "Pandas and NumPy",
        "Natural Language Processing",
        "NLTK",
        "TF-IDF Vectorization",
        "Scikit-learn",
        "Logistic Regression",
        "Multinomial Naive Bayes",
        "Linear Support Vector Machine",
        "Streamlit"
    ]

    for technology in technologies:

        st.markdown(
            f"- {technology}"
        )

    st.divider()

    st.subheader("Project Information")

    st.write("**Dataset:** 2,471 job records")

    st.write("**Classification:** 15 role families")

    st.write("**Selected Model:** Linear SVM")

    st.write("**Accuracy:** 68.48%")

    st.write(
        "**Feature Extraction:** TF-IDF"
    )

    st.caption(
        "This project is an educational machine learning "
        "prototype. Predictions should not be treated "
        "as verified job classifications."
    )

# --------------------------------
# END OF APPLICATION
# --------------------------------
