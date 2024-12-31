import streamlit as st
from PIL import Image
import os

# Title
st.title("🎉 Happy New Year 🎉")

# Input for user's name
name = st.text_input("Enter your name:")

special_wishes = {
    "John": "Wishing you an amazing year ahead filled with success and happiness!",
    "Alice": "Happy New Year, Alice! May your dreams come true this year! 🎆",
    "Michael": "Michael, you’re a star! Wishing you a bright and prosperous New Year! ✨"
}

# Folder containing images
image_folder = "images"  # Replace with the actual folder path where images are stored

# Check if the name is entered
if name:
    # Construct the image file path
    image_path = os.path.join(image_folder, f"{name}.jpg")  # Assuming images are .jpg
    if os.path.exists(image_path):
        # Open the image
        image = Image.open(image_path)
        
        # Display the image and personalized message
        st.image(image, caption=f"{name}'s Image", use_column_width=True)
       
    if name in special_wishes:
        st.markdown(f"## 🎆 {special_wishes[name]} 🎆")
       
        st.markdown(f"## 🎆 Happy New Year, {name}! 🎆")
        st.markdown("Wishing you a year filled with joy, success, and happiness! ✨")
    else:
        st.error(f"Sorry, no image found for {name}. Please make sure your name matches the image file name.")
else:
    st.info("Please enter your name to view your personalized New Year wish.")
