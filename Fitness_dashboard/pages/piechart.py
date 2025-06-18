import streamlit as st
from PIL import Image

st.title(" Pie Chart - Workout Type Distribution")
img = Image.open("C:/Users/sande/OneDrive/Desktop/Final project/gym_fitness_tracker/Fitness_dashboard/charts/pie_chart.jpg")
st.image(img, use_container_width=True)