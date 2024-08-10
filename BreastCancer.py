import streamlit as st

# Streamlit app
st.title('Breast Cancer Prediction Model')
# Bold and large text
st.markdown(
    "<h1 style='text-align: left; font-size: 20px; font-weight: bold;'>By Bonny_Makuwa</h1>",
    unsafe_allow_html=True
)





# Button to show prediction info
if st.button('Prediction Model'):

    # Author Information
    st.write("### Creator Information")
    st.write("**Name:** Bonny Makuwa")
    st.write("**Bio:** Data Scientist with a focus on predictive modeling and data analysis. Proficient in Power BI, Python, SQL, and machine learning techniques. Experienced in creating and optimizing models to drive insights and enhance decision-making processes.")
    st.write("**LinkedIn:** https://www.linkedin.com/in/bonny-makuwa-04a8b6153/")
    st.write("**GitHub:** https://github.com/Bonnymakuwa")
    st.write("**Email:** bonnymakuwa@gmail.com")

    # Project Description
    st.write("""
    ## Project Description
    This breast cancer prediction model is developed to evaluate the likelihood of breast cancer based on various health parameters. It uses commonly recognized thresholds to assess risk levels and provide insights based on user inputs.
    """)


    # User input
    age = st.slider('**Age**', 0, 120, 30)
    sex = st.selectbox('**Sex**', ['Female', 'Male'])
    family_history = st.selectbox('**Family History of Breast Cancer**', ['No', 'Yes'])
    genetic_mutations = st.selectbox('**Genetic Mutations (e.g., BRCA1, BRCA2)**', ['No', 'Yes'])
    hormone_replacement_therapy = st.selectbox('**Hormone Replacement Therapy**', ['No', 'Yes'])
    breast_density = st.selectbox('**Breast Density**', ['Low Density', 'High Density'])
    age_at_first_menstruation = st.slider('**Age at First Menstruation**', 0, 20, 12)
    age_at_first_pregnancy = st.slider('**Age at First Full-Term Pregnancy**', 0, 50, 30)
    menopause_age = st.slider('**Age at Menopause**', 0, 100, 55)
    obesity = st.selectbox('**Obesity (BMI)**', ['< 25 kg/m²', '25-29.9 kg/m²', '≥ 30 kg/m²'])
    alcohol_consumption = st.selectbox('**Alcohol Consumption**', ['Low/Moderate', 'High'])

    # Prediction logic
    def predict_breast_cancer(age, sex, family_history, genetic_mutations, hormone_replacement_therapy, breast_density, age_at_first_menstruation, age_at_first_pregnancy, menopause_age, obesity, alcohol_consumption):
        risk_score = 0
        
        # Age
        if age >= 65:
            risk_score += 2
        elif age >= 45:
            risk_score += 1
        
        # Sex
        if sex == 'Female':
            risk_score += 2
        
        # Family History
        if family_history == 'Yes':
            risk_score += 2
        
        # Genetic Mutations
        if genetic_mutations == 'Yes':
            risk_score += 3
        
        # Hormone Replacement Therapy
        if hormone_replacement_therapy == 'Yes':
            risk_score += 2
        
        # Breast Density
        if breast_density == 'High Density':
            risk_score += 2
        
        # Age at First Menstruation
        if age_at_first_menstruation < 12:
            risk_score += 2
        
        # Age at First Full-Term Pregnancy
        if age_at_first_pregnancy >= 30:
            risk_score += 2
        
        # Age at Menopause
        if menopause_age < 55:
            risk_score += 2
        
        # Obesity (BMI)
        if obesity == '≥ 30 kg/m²':
            risk_score += 3
        elif obesity == '25-29.9 kg/m²':
            risk_score += 2
        
        # Alcohol Consumption
        if alcohol_consumption == 'High':
            risk_score += 2
        
        # Risk assessment based on score
        if risk_score >= 15:
            return "High risk of breast cancer"
        elif risk_score >= 8:
            return "Moderate risk of breast cancer"
        else:
            return "Low risk of breast cancer"

    # Predict breast cancer
    prediction = predict_breast_cancer(
        age,
        sex,
        family_history,
        genetic_mutations,
        hormone_replacement_therapy,
        breast_density,
        age_at_first_menstruation,
        age_at_first_pregnancy,
        menopause_age,
        obesity,
        alcohol_consumption
    )

    # Display results with increased emphasis
    st.markdown(f"""
    ### **Prediction**
    **{prediction}**
    """, unsafe_allow_html=True)
