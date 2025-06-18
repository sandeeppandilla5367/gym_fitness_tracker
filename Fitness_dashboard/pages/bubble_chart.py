import streamlit as st
from PIL import Image

st.title("Bubble Chart - Calories Burned vs Session Duration")
img = Image.open("C:/Users/sande/OneDrive/Desktop/Final project/gym_fitness_tracker/Fitness_dashboard/charts/bubble_chart.jpg")
st.image(img, use_container_width=True)