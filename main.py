import streamlit as st


pages = {
    "Christmas": [
        st.Page("christmas-rand.py", title="Christmas gift randomizer"),
    ],
    "Employee phones": [
        st.Page("employee_records.py", title="Employee's Phone Records"),
        st.Page("create-person.py", title="Create person"),
        st.Page("update-person.py", title="Update person"),
        st.Page("delete-person.py", title="Delete person"),
    ],
    "Resources": [
        st.Page("about.py", title="Learn about me"),
    ],
}

pg = st.navigation(pages)
pg.run()