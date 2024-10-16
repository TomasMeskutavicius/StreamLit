import streamlit as st
import pandas as pd
import requests

BaseURL = 'http://127.0.0.1:8000'

st.title("Employee's Phone Records")

on = st.toggle("Enter manually")

col1, col2 = st.columns(2)

if on:
    with col1:
        name_input = st.text_input(
            "Enter Employee Name: ",
            key="name_input"
        )
    with col2:
        lastname_input = st.text_input(
            "Enter Employee Last Name: ",
            key="last_name_input"
        )

else:
    name_list = requests.get(f"{BaseURL}/get-all-names").json()
    lastname_list = requests.get(f"{BaseURL}/get-all-last-names").json()
    name_list = [item["Name"] for item in name_list]
    lastname_list = [item["LastName"] for item in lastname_list]
    with col1:
        name_input = st.selectbox("Select Employee Name: ", name_list, index=None, placeholder="Select Name...",)
    with col2:
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
    st.write("Please click 'Get Records' to search.")
