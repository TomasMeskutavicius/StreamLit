import streamlit as st
import requests

BaseURL = 'http://127.0.0.1:8000'

st.title("Create Entry")

# Mandatory
Team = st.text_input("Enter Team Name:", key="team_input", placeholder="Enter Team Name:")

# Mandatory
Name = st.text_input("Enter Employee Name:", key="name_input", placeholder="Enter Employee Name:")

# Mandatory
LastName= st.text_input("Enter Employee Last Name:", key="LastName_input", placeholder="Enter Employee Last Name:")

# Mandatory
S_N= st.text_input("Enter Serial Number:", key="S_N_input", placeholder="Enter Serial Number:")

# Mandatory
CurrIMEI= st.text_input("Enter Current IMEI:", key="CurrIMEI_input", placeholder="Enter Current IMEI:")

# Mandatory
orderDate = st.date_input("Enter Order Date:", value="default_value_today", format="YYYY-MM-DD")

# Mandatory
WarrPerriod= st.text_input("Enter Warranty Perriod:", key="WarrPerriod_input", placeholder="Enter Warranty Perriod:")

# Optional
OldIMEI= st.text_input("Enter Old IMEI:", key="OldIMEI_input", placeholder="Enter Old IMEI:")

# Optional
WarrEndDate= st.text_input("Enter Warranty End Date:", key="WarrEndDate_input", placeholder="Enter Warranty End Date:")

# Optional
IMEI2= st.text_input("Enter IMEI2:", key="IMEI2_input", placeholder="Enter IMEI2:")


Create_Record = st.button("Create Record")

if Create_Record is True:
    # Make the API POST                   
    manFields = (f"/create-person?Team={Team}&Name={Name}&LastName={LastName}&S_N={S_N}&CurrIMEI={CurrIMEI}&Orderdate={orderDate}&WarrPerriod={WarrPerriod}")  
    
    if OldIMEI is not None and WarrEndDate is None and IMEI2 is None:
        response = requests.post(f"{BaseURL}{manFields}&OldIMEI={OldIMEI}")
    elif OldIMEI is None and WarrEndDate is not None and IMEI2 is None:
        response = requests.post(f"{BaseURL}{manFields}&WarrEndDate={WarrEndDate}")
    elif OldIMEI is None and WarrEndDate is None and IMEI2 is not None:
        response = requests.post(f"{BaseURL}{manFields}&IMEI2={IMEI2}")
    elif OldIMEI is not None and WarrEndDate is not None and IMEI2 is not None:
        response = requests.post(f"{BaseURL}{manFields}&IMEI2={IMEI2}&WarrEndDate={WarrEndDate}&OldIMEI={OldIMEI}")
    elif OldIMEI is None and WarrEndDate is None and IMEI2 is None:
        response = requests.post(f"{BaseURL}{manFields}")

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        st.success(f'Success, record created: {response.status_code} - {response.reason}')
    else:
        # Handle errors if the request was unsuccessful
        st.error(f"Error: {response.status_code} - {response.reason}")
else:
    st.write("Please click to Create Record.")  # Informative message


