import streamlit as st
import requests

BaseURL = 'http://127.0.0.1:8000'

st.title("about")

response = requests.get(f"{BaseURL}/about")

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Extract the relevant data (adjust as needed)
    extracted_data = data[0]  # Assuming data is in the first element
    # Display the DataFrame in Streamlit
    st.write(extracted_data)
else:
    # Handle errors if the request was unsuccessful
    st.error(f"Error: {response.status_code} - {response.reason}")
