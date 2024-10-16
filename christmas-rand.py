import streamlit as st
import pandas as pd
import requests, datetime

BaseURL = 'http://127.0.0.1:8000'

st.title("Christmas gift randomizer")




name_list = requests.get(f"{BaseURL}/get-all-christmas-names").json()
lastname_list = requests.get(f"{BaseURL}/get-all-christmas-last-names").json()
name_list = [item["Name"] for item in name_list]
lastname_list = [item["LastName"] for item in lastname_list]

name_input = st.selectbox("Select Employee Name: ", name_list, index=None, placeholder="Select Name...",)

lastname_input = st.selectbox("Select Employee Last Name: ", lastname_list, index=None, placeholder="Select Last Name...",)

if name_input is None and lastname_input is None:
    ButtonText = "Get All Records"
else:
    ButtonText = "Get Records"


Get_Records = st.button(ButtonText)

if Get_Records is True:
    # Make the API request
    if lastname_input is None and name_input is not None:
        response = requests.get(f"{BaseURL}/get-details?name={name_input}")
    elif lastname_input is not None and name_input is None:
        response = requests.get(f"{BaseURL}/get-details?LastName={lastname_input}")
    elif lastname_input is not None and name_input is not None:
        response = requests.get(f"{BaseURL}/get-details?name={name_input}&LastName={lastname_input}")
    elif lastname_input is None and name_input is None:
        response = requests.get(f"{BaseURL}/get-all-employees")

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract the relevant data (adjust as needed)
        extracted_data = data[0]  # Assuming data is in the first element
        # Create a DataFrame
        df = pd.DataFrame(data)
        # Display the DataFrame in Streamlit
        st.write(df)
    else:
        # Handle errors if the request was unsuccessful
        st.error(f"Error: {response.status_code} - {response.reason}")
else:
    st.write("Please click 'Get Records' to search.")  # Informative message

