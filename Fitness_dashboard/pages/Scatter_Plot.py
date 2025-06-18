import streamlit as st
from PIL import Image

st.title("Scatter Plot - Avg BPM vs Max BPM")
img = Image.open("C:/Users/sande/OneDrive/Desktop/Final project/gym_fitness_tracker/Fitness_dashboard/charts/scatter_plot.jpg")
st.image(img, use_container_width=True)