import streamlit as st
from PIL import Image

st.title("Bar Graph - Calories Burned by Workout Type")
img = Image.open("C:/Users/sande/OneDrive/Desktop/Final project/gym_fitness_tracker/Fitness_dashboard/charts/bar_graph.jpg")
st.image(img, use_container_width=True)