import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Create directory for saving charts
os.makedirs('charts', exist_ok=True)

# Load data
df = pd.read_csv("cleaned_gym_members_exercise_tracking.csv")

# 1. Pie Chart: Workout Type Distribution
plt.figure(figsize=(8, 8))
workout_counts = df['Workout_Type'].value_counts()
plt.pie(workout_counts, labels=workout_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Workout Type Distribution')
plt.axis('equal')
plt.savefig('charts/pie_chart.jpg', dpi=300, bbox_inches='tight')
plt.close()

# 2. Bar Graph: Average Calories Burned by Workout Type
plt.figure(figsize=(10, 6))
sns.barplot(x='Workout_Type', y='Calories_Burned', data=df, ci=None)
plt.xticks(rotation=45)
plt.title('Average Calories Burned by Workout Type')
plt.xlabel('Workout Type')
plt.ylabel('Calories Burned')
plt.tight_layout()
plt.savefig('charts/bar_graph.jpg', dpi=300, bbox_inches='tight')
plt.close()

# 3. Scatter Plot: Avg BPM vs Max BPM
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Max_BPM', y='Avg_BPM', hue='Workout_Type', data=df, alpha=0.7)
plt.title('Avg BPM vs Max BPM by Workout Type')
plt.grid(True)
plt.tight_layout()
plt.savefig('charts/scatter_plot.jpg', dpi=300, bbox_inches='tight')
plt.close()

# 4. Histograms: Session Duration and Calories Burned
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.histplot(df['Session_Duration (hours)'], ax=axes[0], kde=True)
sns.histplot(df['Calories_Burned'], ax=axes[1], kde=True)
axes[0].set_title('Session Duration Distribution')
axes[1].set_title('Calories Burned Distribution')
plt.tight_layout()
plt.savefig('charts/histograms.jpg', dpi=300, bbox_inches='tight')
plt.close()

# 5. Bubble Chart: Calories Burned vs Session Duration (size = BMI)
plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    df['Session_Duration (hours)'],
    df['Calories_Burned'],
    s=df['BMI'] * 10,
    c=df['Avg_BPM'],
    cmap='viridis',
    alpha=0.6,
    edgecolors="w",
    linewidth=0.5
)
plt.colorbar(scatter, label='Avg BPM')
plt.title('Bubble Chart: Calories Burned vs Session Duration (Size = BMI)')
plt.xlabel('Session Duration (hours)')
plt.ylabel('Calories Burned')
plt.grid(True)
plt.tight_layout()
plt.savefig('charts/bubble_chart.jpg', dpi=300, bbox_inches='tight')
plt.close()

# 6. Area Chart: Cumulative Calories Burned over Session Duration
df_sorted = df.sort_values(by='Session_Duration (hours)')
plt.figure(figsize=(10, 6))
plt.fill_between(df_sorted['Session_Duration (hours)'], df_sorted['Calories_Burned'], color="skyblue", alpha=0.4)
plt.plot(df_sorted['Session_Duration (hours)'], df_sorted['Calories_Burned'], color="Red", alpha=0.6, linewidth=2)
plt.title('Cumulative Calories Burned Over Session Duration')
plt.xlabel('Session Duration (hours)')
plt.ylabel('Calories Burned')
plt.grid(True)
plt.tight_layout()
plt.savefig('charts/area_chart.jpg', dpi=300, bbox_inches='tight')
plt.close()

print(" Charts saved to 'charts/' folder.")
