import streamlit as st
import requests

# Display the image
st.image('cover.jpg', caption='Image Caption', use_column_width=True)
# Customized title using HTML tags
st.markdown('<h1 style="color: blue; font-style: italic;">Patient Prediction Application</h1>', unsafe_allow_html=True)

age = st.number_input('Age')
bmi = st.number_input('BMI Index')
bp = st.number_input('Blood Pressure')

# Handle when the user clicks the "Predict" button
if st.button('Predict'):

    # Send a POST request to your API
    url = "http://localhost:8000/predict"
    data = {
        "age": age,
        "bmi": bmi,
        "bp": bp
    }
    response = requests.post(url, json=data)

    # Handle the response from the API
    if response.status_code == 200:
        result = response.json()
        prediction = result['prediction']
        conclusion = result['conclusion']
        st.write('Prediction:', prediction)
        st.write('Conclusion:', conclusion)
    else:
        st.error('An error occurred while sending the request to the API.')