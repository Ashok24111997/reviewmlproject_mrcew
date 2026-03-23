import streamlit as st
from datetime import date

st.title("Vote for Future")
st.subheader("Enter the basic details")

name = st.text_input("Enter your name")

dob = st.date_input(
    "Select your DOB",
    value=None,  
    min_value=date(1950,1,1) ,                       # important: no default value
    max_value=date.today()
)

# Button
if st.button("Check Eligibility"):
    if not name or not dob:
        st.warning("Please enter all details")
    else:
        today = date.today()

        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        st.write("Your Age:", age)

        if age >= 18:
            st.success("✅ You are eligible to vote")
        else:
            st.error("❌ You are not eligible to vote")