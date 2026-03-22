import streamlit as st

st.set_page_config(page_title="Student App", page_icon="🎓")

st.title("🎓 Student Dashboard")

st.sidebar.title("Menu")
choice = st.sidebar.selectbox("Navigate", ["Home", "Result"])

if choice == "Home":
    st.markdown("<h2 style='color:green;'>Welcome Student</h2>", unsafe_allow_html=True)

elif choice == "Result":
    marks = st.number_input("Enter Marks")

    if st.button("Check Result"):
        if marks >= 35:
            st.success("Pass ✅")
            st.balloons()
        else:
            st.error("Fail ❌")