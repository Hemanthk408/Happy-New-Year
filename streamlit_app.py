import streamlit as st
from PIL import Image

# Title
st.title("🎉 Happy New Year 🎉")

# Input for user's name
name = st.text_input("Enter your name:")

# File uploader for image
uploaded_file = st.file_uploader("Upload your image:", type=["jpg", "jpeg", "png"])

# Display Happy New Year wish if both name and image are provided
if name and uploaded_file:
    # Open the uploaded image
    image = Image.open(uploaded_file)
    
    # Display the image and personalized message
    st.image(image, caption=f"{name}'s Image", use_column_width=True)
    st.markdown(f"## 🎆 Happy New Year, {name}! 🎆")
    st.markdown("Wishing you a year filled with joy, success, and happiness! ✨")
elif not name:
    st.warning("Please enter your name.")
elif not uploaded_file:
    st.warning("Please upload an image.")
