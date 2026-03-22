import streamlit as st
from datetime import date

st.set_page_config(page_title="Student App 🎓", page_icon="🎓")

# Sidebar menu
st.sidebar.title("📌 Menu")
menu = st.sidebar.selectbox("Navigate", ["Home", "Student Form", "About"])

# ---------------- HOME ----------------
if menu == "Home":
    st.title("🏠 Welcome")
    st.write("This is a Student Dashboard App")
   
# ---------------- FORM ----------------
elif menu == "Student Form":
    st.title("🎓 Student Form")

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("👤 Name")
            blood_group = st.selectbox(
                "🩸 Blood Group",
                ["Select", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
            )

        with col2:
            dob = st.date_input(
                "🎂 DOB",
                min_value=date(2000, 1, 1),
                max_value=date.today()
            )

    if st.button("Submit"):
        if not name or blood_group == "Select":
            st.warning("⚠️ Fill all details")
        else:
            st.success("✅ Submitted Successfully")
            st.write("👤 Name:", name)
            st.write("🎂 DOB:", dob)
            st.write("🩸 Blood Group:", blood_group)
            st.balloons()

# ---------------- ABOUT ----------------
elif menu == "About":
    st.title("ℹ️ About")
    st.write("This app is built using Streamlit.")
    st.info("Simple project for learning sidebar navigation.")