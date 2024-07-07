
import streamlit as st
import pickle
from PIL import Image
import pandas as pd

# Load the trained model and preprocessor
loaded_model = pickle.load(open('rand.sav', 'rb'))
loaded_preprocessor = pickle.load(open('Scale (2).sav', 'rb'))

# Function to preprocess input data
def preprocess_input(data):
    processed_data = loaded_preprocessor.transform(data)
    return processed_data

# Function to make predictions

def predict_loan_status(data):
    processed_data = preprocess_input(data)
    prediction = loaded_model.predict(processed_data)
    return prediction
#streamlit app layout
def main():

    st.title('Loan Status Prediction')

    # Sidebar with user input form
    st.sidebar.header("User Input")
    Gender = st.sidebar.selectbox("gender",['male','female'])
    if Gender == 'male':
        Gender=1
    elif Gender == 'female':
        Gender=0
    Education = st.sidebar.selectbox("Education	", ['Graduate','Not Graduate'])

    if Education == 'Graduate':
        Education=0
    elif Education == 'Not Graduate':
        Education=1
    Self_Employed =st.sidebar.selectbox('employed',['yes','no'])
    if Self_Employed== 'no':
        Self_Employed=0
    elif Self_Employed == 'yes':
        Self_Employed=1
    ApplicantIncome =st.sidebar.slider('Income',0,100,10000)
    CoapplicantIncome = st.sidebar.slider('Co applicant Income',0,100,100000)
    LoanAmount = st.sidebar.slider('loan amount',0,100,1000)
    Loan_Amount_Term =  st.sidebar.slider('loan amount term ',0,100,1000)
    Credit_History = st.sidebar.selectbox('Credit_History',['1','0'])
    Property_Area = st.sidebar.selectbox('Property_Area',['Rural','Urban','Semiurban'])

    if Property_Area == 'Rural':
        Property_Area=0
    elif Property_Area =='Urban':
        Property_Area=2
    else:
        Property_Area=1
    image = Image.open('10191052.jpg')
    st.image(image,width=750)

    abc = [Gender,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]

    # Predict button
    if st.sidebar.button("Predict"):
        prediction = predict_loan_status([abc])
        # Display the prediction
        st.subheader("Prediction:")
        if prediction == 0:
            st.success("applicant not loan approved.")
        else:
            st.info("applicant loan approved.")


main()