import matplotlib.pyplot as plt
import numpy as np

# Given data
data = {
    "calories": "2763.9 kcal",
    "carbohydrates": "320.0 g",
    "protein": "155.03 g",
    "fat": "87.19 g",
}

# Function to extract numerical values
def extract_value(value):
    return float(value.split()[0])

# Extract numerical values for each nutrient
values = [extract_value(data[nutrient]) for nutrient in data]

# Set a threshold to prevent negative values
values = np.maximum(values, 0)

# Labels and colors for the pie chart
labels = list(data.keys())
colors = ['#FFA07A', '#98FB98', '#FF6347', '#87CEEB']

# Plot a pie chart
plt.figure(figsize=(8, 8))
plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops=dict(width=0.4))
plt.title('Nutrient Distribution', fontsize=16, color='grey')

# Show the plot
plt.show()