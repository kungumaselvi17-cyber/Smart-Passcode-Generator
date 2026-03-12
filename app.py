import streamlit as st
from password_utils import generate_password, check_strength

st.title("🔐 Smart Password Generator")

length = st.slider("Password Length", 4, 32, 12)

upper = st.checkbox("Include Uppercase")
lower = st.checkbox("Include Lowercase", value=True)
numbers = st.checkbox("Include Numbers", value=True)
symbols = st.checkbox("Include Symbols")

if st.button("Generate Password"):

    password = generate_password(length, upper, lower, numbers, symbols)

    st.success(f"Generated Password: {password}")

    strength = check_strength(password)
    st.info(f"Password Strength: {strength}")
