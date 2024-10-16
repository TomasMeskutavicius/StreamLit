import streamlit as st
import requests

st.title("Delete person")

BaseURL = 'http://127.0.0.1:8000'

Name = st.text_input("Enter Employee Name:", key="name_input_1", placeholder="Required field")
if not Name:
    st.error("Please enter the employee's first name.")

LastName = st.text_input("Enter Employee Last Name:", key="last_name_input_1", placeholder="Required field")
if not LastName:
    st.error("Please enter the employee's last name.")

Create_Record = st.button("Delete record")

if Create_Record is True:
    # Make the API DELETE
    response = requests.delete(f"{BaseURL}/delete-person?Name={Name}&LastName={LastName}")
    # Check if the request was successful
    if response.status_code == 200:
        st.success(f'Success, record deleted: {response.status_code} - {response.reason}')
    else:
        # Handle errors if the request was unsuccessful
        st.error(f"Error: {response.status_code} - {response.reason}")
else:
    st.write("Please click to delete record.")