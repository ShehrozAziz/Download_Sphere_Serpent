import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Sphere Serpent - Game Download",
    page_icon="🐍",
    layout="centered"
)

# Title and Description
st.title("🐍 Sphere Serpent")
st.markdown("""
### A Revolutionary Twist on the Classic Snake Game!
Experience the classic snake game like never before! Navigate the globe and collect special coins to change your size, speed, or even flip your controls. The game is developed in Unity, ensuring a smooth and engaging experience.
""")

# Add a video
st.video("snake.mp4")  # Replace with your game's video link

# Download Section
st.subheader("Download the Game")
st.markdown("""
Sphere Serpent is available for download now! Click the button below to start your adventure.
""")

# Provide the direct download link from Google Drive
download_link = "https://github.com/ShehrozAziz/Snake-On-Globe/archive/refs/tags/One.zip"
st.markdown(
    f'<a href="{download_link}" target="_blank">'
    '<button style="background-color:green;color:white;padding:10px 20px;border:none;border-radius:5px;cursor:pointer;">'
    'Download Sphere Serpent</button>'
    '</a>',
    unsafe_allow_html=True
)

# Footer
st.markdown("---")
st.markdown("Developed by Shehroz Aziz. Powered by Unity.")
