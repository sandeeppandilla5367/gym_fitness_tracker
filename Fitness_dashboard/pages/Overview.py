# pages/Overview.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Gym Members Exercise Tracking - Overview")
st.markdown("This page provides an overview of the dataset: `cleaned_gym_members_exercise_tracking.csv`")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("C:/Users/sande/OneDrive/Desktop/Final project/gym_fitness_tracker/Fitness_dashboard/data/cleaned_gym_members_exercise_tracking.csv")

df = load_data()

# Show first 5 rows
st.subheader("First 5 Rows of Data")
st.write(df.head())

# Summary Statistics
st.subheader("Summary Statistics")
st.write(df.describe(include='all'))

# Missing Values
st.subheader("Missing Values")
st.write(df.isnull().sum())

# Data Types
st.subheader("Data Types")
st.write(df.dtypes)

# Optional Visualizations
st.subheader("Distribution of Key Metrics")

# Distribution of Age
fig, ax = plt.subplots()
sns.histplot(df['Age'], bins=10, kde=True, ax=ax)
ax.set_title("Age Distribution")
st.pyplot(fig)

# Distribution of Calories Burned
fig, ax = plt.subplots()
sns.histplot(df['Calories_Burned'], bins=20, kde=True, ax=ax)
ax.set_title("Calories Burned Distribution")
st.pyplot(fig)

# Workout Type Distribution
st.subheader("Workout Type Distribution")
fig, ax = plt.subplots()
df['Workout_Type'].value_counts().plot(kind='bar', ax=ax)
ax.set_title("Workout Type Counts")
st.pyplot(fig)