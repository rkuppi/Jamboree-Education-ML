import streamlit as st
import pickle
import numpy as np

st.title("Jomboree Education")
st.subheader("Predict the change of getting admission to a University")

# GRE Score	TOEFL Score	University Rating	SOP	LOR	CGPA	Research
gre_score = st.number_input('Enter your GRE Score', min_value=260, max_value=340)
toefel_score = st.number_input('Enter your TOEFL Score', min_value=90, max_value=120)
university_rating = st.number_input('Enter your University Rating', min_value=1, max_value=5)
sop_score = st.number_input('Enter your SOP Score', min_value=1, max_value=5)
lor_score = st.number_input('Enter your LOR Score', min_value=1, max_value=5)
cgpa = st.slider('Select your CGPA',min_value=6.5,max_value=10.0,value=6.5,step=0.1)
research = binary_input = st.selectbox('Do you have research experience yes/No', [0, 1])

X_test = np.array([gre_score, toefel_score, university_rating, sop_score, lor_score, cgpa, research]).reshape(1,-1)

with open(r'\\Artifacts\\StandardScaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open(r'\\Artifacts\\LinearRegressionmodel.pkl', 'rb') as file:
    model = pickle.load(file)

if(st.button("Submit")):
    scaled_data = scaler.transform(X_test)
    prediction = model.predict(scaled_data)
    prediction = round(prediction[0] *100, 2)
    st.text(f"Chance of getting Admit for the university for the given score will be {prediction} %")