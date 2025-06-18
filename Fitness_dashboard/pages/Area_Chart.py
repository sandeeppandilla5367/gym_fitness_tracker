import streamlit as st
from PIL import Image

st.title(" Area Chart - Cumulative Calories Burned")
img = Image.open("C:/Users/sande/OneDrive/Desktop/Final project/gym_fitness_tracker/Fitness_dashboard/charts/area_chart.jpg")
st.image(img, use_container_width=True)