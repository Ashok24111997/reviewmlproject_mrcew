import streamlit as st
from datetime import date

st.title("Student Form 🎓")

with st.form("student_form"):
    name = st.text_input("Name")

    dob = st.date_input(
        "DOB",
        min_value=date(2000, 1, 1),
        max_value=date.today()
    )

    blood_group = st.selectbox(
        "Blood Group",
        ["Select", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    )

    submit = st.form_submit_button("Submit")

if submit:
    if not name or blood_group == "Select":
        st.warning("Fill all details ⚠️")
    else:
        st.success("Submitted ✅")
        st.write(name, dob, blood_group)