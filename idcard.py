import streamlit as st
from datetime import date

st.title("🪪 ID Card Generator")

# Inputs
name = st.text_input("Enter your name")

dob = st.date_input(
    "Select your DOB",
    value=None,
    min_value=date(1950,1,1),
    max_value=date.today()
)

photo = st.file_uploader("Upload your photo", type=["jpg", "png", "jpeg"])

# Button
if st.button("Generate ID Card"):
    if not name or not dob or not photo:
        st.warning("Please fill all details and capture photo")
    else:
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        st.markdown("## 🪪 Your ID Card")

        # Card Layout
        col1, col2 = st.columns(2)

        with col1:
            st.image(photo, width=150)

        with col2:
            st.write(f"**Name:** {name}")
            st.write(f"**Age:** {age}")

        st.success("ID Card Generated Successfully ✅")