import streamlit as st
from datetime import date

# Page config
st.set_page_config(page_title="Student Details 🎓", page_icon="🎓")


st.markdown("<h1 style='text-align: center; color: darkblue;'>🎓 Student Details Form</h1>", unsafe_allow_html=True)

# Form container
with st.container():
    st.markdown("### 👤 Enter Your Details")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Enter Name")

        blood_group = st.selectbox(
            "🩸 Blood Group",
            ["Select", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        )

    with col2:
        dob = st.date_input(
            "🎂 Date of Birth",
            min_value=date(2000, 1, 1),
            max_value=date.today()
        )

# Submit button
if st.button("🚀 Submit"):
    if name == "" or blood_group == "Select":
        st.warning("⚠️ Please fill all details")
    else:
        st.success("✅ Submitted Successfully!")
        st.write("👤 Name:", name)
        st.write("🎂 DOB:", dob)
        st.write("🩸 Blood Group:", blood_group)
        st.balloons()