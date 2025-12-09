import streamlit as st
import pandas as pd
import joblib
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Smart Loan Predictor AI",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. ENHANCED CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Main Background with Gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    /* Glassmorphism Container */
    .main .block-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    
    /* Sidebar Glassmorphism */
    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(12px);
        border-right: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: transparent;
    }
    
    /* Headers */
    h1, h2, h3 {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    /* Subheaders */
    .stMarkdown h3 {
        color: #f0f0f0;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    
    /* Labels */
    label {
        color: #ffffff !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
    }
    
    /* Input Fields Glassmorphism */
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > div,
    .stSlider > div > div > div,
    .stRadio > div {
        background: rgba(255, 255, 255, 0.2) !important;
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 12px !important;
        color: #ffffff !important;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > div:focus {
        border: 2px solid rgba(255, 255, 255, 0.6) !important;
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.3);
        transform: scale(1.02);
    }
    
    /* Button - Premium Gradient */
    div.stButton > button {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        width: 100%;
        border-radius: 15px;
        height: 60px;
        font-size: 22px;
        font-weight: 700;
        border: none;
        box-shadow: 0 10px 30px rgba(245, 87, 108, 0.4);
        transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    
    div.stButton > button:hover {
        background: linear-gradient(135deg, #f5576c 0%, #f093fb 100%);
        transform: translateY(-5px) scale(1.03);
        box-shadow: 0 15px 40px rgba(245, 87, 108, 0.6);
    }
    
    div.stButton > button:active {
        transform: translateY(-2px) scale(0.98);
    }
    
    /* Success Box - Glassmorphism */
    .success-box {
        padding: 30px;
        background: rgba(72, 219, 134, 0.2);
        backdrop-filter: blur(15px);
        color: #ffffff;
        border-left: 6px solid #48db86;
        border-radius: 20px;
        font-size: 20px;
        box-shadow: 0 8px 32px rgba(72, 219, 134, 0.3);
        animation: slideIn 0.5s ease-out;
        border: 1px solid rgba(72, 219, 134, 0.3);
    }
    
    .success-box h3 {
        color: #48db86;
        margin-bottom: 15px;
        font-size: 32px;
    }
    
    /* Error Box - Glassmorphism */
    .error-box {
        padding: 30px;
        background: rgba(255, 82, 82, 0.2);
        backdrop-filter: blur(15px);
        color: #ffffff;
        border-left: 6px solid #ff5252;
        border-radius: 20px;
        font-size: 20px;
        box-shadow: 0 8px 32px rgba(255, 82, 82, 0.3);
        animation: slideIn 0.5s ease-out;
        border: 1px solid rgba(255, 82, 82, 0.3);
    }
    
    .error-box h3 {
        color: #ff5252;
        margin-bottom: 15px;
        font-size: 32px;
    }
    
    /* Slide In Animation */
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Info Box */
    .stAlert {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: #ffffff;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #f093fb 0%, #f5576c 100%);
        border-radius: 10px;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 10px;
        color: #ffffff !important;
        font-weight: 600;
    }
    
    /* Slider */
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #f093fb 0%, #f5576c 100%);
    }
    
    /* Radio Buttons */
    .stRadio > div {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(8px);
        padding: 15px;
        border-radius: 12px;
    }
    
    /* Logo Container */
    .logo-container {
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    /* Title Animation */
    .main-title {
        animation: fadeInDown 0.8s ease-out;
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Card Effect for Columns */
    .element-container {
        transition: transform 0.3s ease;
    }
    
    .element-container:hover {
        transform: translateY(-2px);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: rgba(255, 255, 255, 0.8);
        font-size: 14px;
        margin-top: 40px;
        padding: 20px;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
    }
    
    /* Warning */
    .stWarning {
        background: rgba(255, 193, 7, 0.2);
        backdrop-filter: blur(10px);
        border-left: 4px solid #ffc107;
        color: #ffffff;
        border-radius: 10px;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        margin: 30px 0;
    }
    
    /* Select Slider */
    .stSelectSlider > div > div {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(8px);
        border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOAD MODEL ---
@st.cache_resource
def load_model():
    try:
        return joblib.load('loan_model.pkl')
    except:
        return None

model = load_model()

# --- 4. HEADER SECTION ---
col1, col2 = st.columns([1, 5])
with col1:
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/4149/4149665.png", width=100)
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="main-title">', unsafe_allow_html=True)
    st.title("🏦 Smart Loan Approval System")
    st.markdown("### 🤖 AI-Powered Risk Assessment Tool")
    st.markdown('</div>', unsafe_allow_html=True)

if model is None:
    st.error("⚠️ Error: 'loan_model.pkl' file not found! Please check the folder.")
    st.stop()

st.markdown("---")

# --- 5. INPUT FORM ---
st.sidebar.markdown("### 👤 Applicant Profile")
st.sidebar.info("📋 Please fill all details accurately for best results.")

# Sidebar Inputs (Categorical)
gender = st.sidebar.radio("👥 Gender", ["Male", "Female"], horizontal=True)
married = st.sidebar.selectbox("💑 Marital Status", ["No", "Yes"])
dependents = st.sidebar.selectbox("👨‍👩‍👧‍👦 Dependents", ["0", "1", "2", "3+"])
education = st.sidebar.selectbox("🎓 Education", ["Graduate", "Not Graduate"])
self_employed = st.sidebar.selectbox("💼 Self Employed", ["No", "Yes"])
property_area = st.sidebar.select_slider("🏘️ Property Area", options=["Rural", "Semiurban", "Urban"])

# Main Page Inputs (Numerical)
c1, c2 = st.columns(2)

with c1:
    st.subheader("💰 Financial Details")
    applicant_income = st.number_input("💵 Applicant Income ($)", min_value=0, value=5000, step=100)
    coapplicant_income = st.number_input("💳 Coapplicant Income ($)", min_value=0, value=0, step=100)
    loan_amount = st.slider("💸 Loan Amount (in Thousands)", 10, 700, 120)

with c2:
    st.subheader("📝 Loan Terms")
    loan_amount_term = st.selectbox("📅 Loan Term (Months)", [360, 180, 480, 300, 84, 60])
    credit_input = st.radio("⭐ Credit History", ["Good (Debts Paid)", "Bad (Defaults)"], horizontal=True)
    credit_history = 1.0 if "Good" in credit_input else 0.0

# --- 6. DATA PROCESSING ---
data = {
    'Gender': gender,
    'Married': married,
    'Dependents': dependents,
    'Education': education,
    'Self_Employed': self_employed,
    'ApplicantIncome': applicant_income,
    'CoapplicantIncome': coapplicant_income,
    'LoanAmount': loan_amount,
    'Loan_Amount_Term': loan_amount_term,
    'Credit_History': credit_history,
    'Property_Area': property_area
}

df = pd.DataFrame(data, index=[0])

# Feature Engineering
df['Total_Income'] = df['ApplicantIncome'] + df['CoapplicantIncome']
df['Loan_Term_Years'] = df['Loan_Amount_Term'] / 12

# --- 7. PREDICTION & DISPLAY ---
st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 Analyze Loan Eligibility"):
    
    # Progress Bar Animation
    progress_text = "🔍 Analyzing credit score..."
    my_bar = st.progress(0, text=progress_text)
    
    stages = [
        "🔍 Analyzing credit score...",
        "📊 Checking financial history...",
        "🏦 Verifying bank records...",
        "🤖 AI processing data...",
        "✅ Finalizing results..."
    ]
    
    for i, stage in enumerate(stages):
        for percent in range(i * 20, (i + 1) * 20):
            time.sleep(0.02)
            my_bar.progress(percent + 1, text=stage)
    
    my_bar.empty()

    # Prediction
    try:
        prediction = model.predict(df)
        probability = model.predict_proba(df)[:, 1][0]
        
        threshold = 0.07
        
        st.markdown("---")
        
        if probability >= threshold:
            st.balloons()
            st.markdown(f"""
                <div class="success-box">
                    <h3>✅ Loan Approved!</h3>
                    <p style="font-size: 18px; margin: 10px 0;">🎉 Congratulations! Your profile meets our lending criteria.</p>
                    <p style="font-size: 22px; font-weight: 600; margin-top: 15px;">
                        📈 <b>Confidence Score:</b> {probability:.2%}
                    </p>
                    <p style="font-size: 16px; margin-top: 10px; opacity: 0.9;">
                        You can proceed with the loan application process.
                    </p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="error-box">
                    <h3>❌ Loan Rejected</h3>
                    <p style="font-size: 18px; margin: 10px 0;">😔 Unfortunately, your risk score is too high at this moment.</p>
                    <p style="font-size: 22px; font-weight: 600; margin-top: 15px;">
                        📉 <b>Approval Probability:</b> {probability:.2%}
                    </p>
                    <p style="font-size: 16px; margin-top: 10px; opacity: 0.9;">
                        Minimum required: 7% | Current: {probability:.2%}
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            # Why rejected?
            with st.expander("🔍 Why was my application rejected?"):
                if credit_history == 0.0:
                    st.warning("⚠️ **Credit History:** Your credit history shows defaults. This is a critical factor in loan approval.")
                if df['Total_Income'].iloc[0] < 3000:
                    st.warning("⚠️ **Income Level:** Your total household income may be insufficient for the requested loan amount.")
                if loan_amount > 500:
                    st.warning("⚠️ **Loan Amount:** The requested amount is quite high. Consider applying for a lower amount.")
                
                st.info("💡 **Tip:** Improve your credit score and consider reapplying after 3-6 months.")
                
    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")

# Footer
st.markdown("---")
st.markdown("""
    <div class="footer">
        <p style="font-size: 16px; margin-bottom: 10px;">
            <b>Smart Loan Predictor AI</b> - Powered by Advanced Machine Learning
        </p>
        <p>Developed with ❤️ using Streamlit & Scikit-Learn</p>
        <p style="font-size: 12px; opacity: 0.7; margin-top: 10px;">
            © 2024 All Rights Reserved | For Educational Purposes Only
        </p>
    </div>
""", unsafe_allow_html=True)