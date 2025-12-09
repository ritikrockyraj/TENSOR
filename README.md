# 🏦 Smart Loan Eligibility Predictor

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 🚀 Live Demo
**Check out the live app here:** [LINK_WILL_GO_HERE](put_your_link_here)

---

## 📖 Project Overview
The **Smart Loan Eligibility Predictor** is an end-to-end Machine Learning web application designed to automate the loan approval process for banking institutions. 

Manual loan assessment is time-consuming and prone to human error. This project solves that problem by analyzing applicant data (income, credit history, dependents) to predict **Loan Approval Status** with high precision.

---

## 🧠 Model Development Process

The project followed a rigorous Data Science lifecycle to ensure reliability:

### 1. Exploratory Data Analysis (EDA) & Cleaning
- **Handling Missing Values:** Imputed numerical missing values with `Median` and categorical with `Mode`.
- **Outlier Treatment:** Analyzed income distribution and handled extreme skewness using log transformations.
- **Class Imbalance:** Addressed the imbalance in the target variable using `class_weight='balanced'` techniques.

### 2. Feature Engineering
To improve model performance, new features were derived:
- **`Total_Income`**: Combined Applicant and Co-applicant income to get a holistic view of financial stability.
- **`Loan_Term_Years`**: Converted months to years for better interpretability.
- **Encoding:** Used One-Hot Encoding and Label Encoding for categorical variables like Gender and Property Area.

### 3. Model Selection & Tuning
- Tested multiple algorithms: **Logistic Regression**, **Random Forest**, and **Decision Trees**.
- **Final Model:** Selected **Logistic Regression (with Feature Engineering)** as it provided the best balance between bias and variance ("Good Fit").

---

## 📊 Model Performance & Results

We prioritized **Recall** over Accuracy. In banking, **False Negatives** (predicting a defaulter as 'Safe') are dangerous. Therefore, the model is tuned to catch potential defaulters aggressively.

| Metric | Score | Description |
| :--- | :--- | :--- |
| **Recall (Sensitivity)** | **~98%** | The model catches 98% of risky applicants. |
| **Accuracy** | **~82%** | Overall correctness of predictions. |
| **F2 Score** | **~0.94** | Weighted score favoring Recall. |
| **ROC-AUC** | **High** | Excellent separation between classes. |

### 📉 Business Logic & Optimization
- **Threshold Tuning:** The standard prediction threshold is 0.5. However, to minimize financial risk, we optimized the decision threshold to **0.07**.
- **Reasoning:** It is safer for the bank to double-check a safe applicant than to approve a risky loan. This strict threshold ensures that only highly eligible candidates get an automatic "Approved" signal.

---

## ✨ App Features
- **Real-Time Prediction:** Instant assessment based on user inputs.
- **Smart UI:** Professional "Fintech" style interface built with Streamlit.
- **Explainability:** - 🟢 **Success:** Displays confidence score for approved loans.
  - 🔴 **Rejection Logic:** Explicitly tells the user *why* they were rejected (e.g., "Low Income", "Bad Credit History").

---

## 🛠️ Tech Stack
- **Frontend:** Streamlit (Python Framework)
- **Machine Learning:** Scikit-Learn (Pipeline, Logistic Regression)
- **Data Processing:** Pandas, NumPy
- **Model Persistence:** Joblib

---

## ⚙️ How to Run Locally

1. **Clone the repository**
   ```bash
   git clone [https://github.com/your-username/loan-prediction-app.git](https://github.com/your-username/loan-prediction-app.git)
