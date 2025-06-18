# main_app.py
import streamlit as st

st.set_page_config(page_title="Fitness Dashboard", layout="wide")

st.title("Fitness & Health Analytics Dashboard")
st.markdown("""
Welcome to the Gym Member Fitness Dashboard.  
Use the sidebar to navigate between different visualizations.
""")

st.sidebar.title("Navigation")
st.sidebar.markdown("Select a section:")

import streamlit as st
from PIL import Image

st.title("Pie Chart - Workout Type Distribution")
img = Image.open("C:/Users/sande/OneDrive/Desktop/Final project/gym_fitness_tracker/Fitness_dashboard/charts/pie_chart.jpg")
st.image(img, use_container_width=True)

import streamlit as st
from PIL import Image

st.title("Bar Graph - Calories Burned by Workout Type")
img = Image.open("C:/Users/sande/OneDrive/Desktop/Final project/gym_fitness_tracker/Fitness_dashboard/charts/bar_graph.jpg")
st.image(img, use_container_width=True)

import streamlit as st
from PIL import Image

st.title("Scatter Plot - Avg BPM vs Max BPM")
img = Image.open("C:/Users/sande/OneDrive/Desktop/Final project/gym_fitness_tracker/Fitness_dashboard/charts/scatter_plot.jpg")
st.image(img, use_container_width=True)

import streamlit as st
from PIL import Image

st.title("Histograms - Session Duration & Calories Burned")
img = Image.open("C:/Users/sande/OneDrive/Desktop/Final project/gym_fitness_tracker/Fitness_dashboard/charts/histograms.jpg")
st.image(img, use_container_width=True)

import streamlit as st
from PIL import Image

st.title("Bubble Chart - Calories Burned vs Session Duration")
img = Image.open("C:/Users/sande/OneDrive/Desktop/Final project/gym_fitness_tracker/Fitness_dashboard/charts/bubble_chart.jpg")
st.image(img, use_container_width=True)

import streamlit as st
from PIL import Image

st.title("Area Chart - Cumulative Calories Burned")
img = Image.open("C:/Users/sande/OneDrive/Desktop/Final project/gym_fitness_tracker/Fitness_dashboard/charts/area_chart.jpg")
st.image(img, use_container_width=True)