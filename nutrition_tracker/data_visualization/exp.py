# Certainly! Here are a few creative ideas to enhance the nutrient distribution visualization:
#
# 1. **Doughnut Chart with Subplots:**
#    Use a doughnut chart to visualize the nutrient distribution and add subplots for additional information, such as calories or other nutrients.
#
# 2. **Radar Chart:**
#    Represent each nutrient as a point on a radar chart. This can provide a unique and visually interesting perspective on the nutrient distribution.
#
# 3. **Gradient Bar Chart:**
#    Use a gradient color scheme for the bars, where the color intensity varies based on the nutrient amount. This can create a visually appealing effect.
#
# 4. **Interactive Plot:**
#    Build an interactive plot using tools like Plotly or Bokeh. This allows users to hover over the chart for detailed information on each nutrient.
#
# 5. **3D Bar Chart:**
#    Represent the nutrient distribution in a 3D bar chart for a more dynamic and engaging visualization.
#
# 6. **Bubble Chart:**
#    Create a bubble chart where each nutrient is represented by a bubble, and the size of the bubble corresponds to the nutrient amount.
#
# 7. **Animated Chart:**
#    Use animation to show how the nutrient distribution changes over time or in different meals. This can be done with libraries like Matplotlib or Plotly.
#
# 8. **Custom Icons:**
#    Replace traditional bars with custom icons that represent each nutrient. For example, use a wheat icon for carbohydrates, a steak icon for protein, and an olive oil icon for fat.
#
# 9. **Gradient Background:**
#    Apply a gradient color background to the chart, creating a visually striking effect that complements the nutrient distribution.
#
# 10. **Word Cloud:**
#     Use a word cloud to visualize the most prominent nutrients. The size of each nutrient in the word cloud can represent its quantity.
#
# Feel free to choose the idea that aligns with your preferences and the story you want to convey with the nutrient distribution visualization. You can implement these ideas using various Python visualization libraries like Matplotlib, Plotly, Seaborn, or any other library you are comfortable with.




import matplotlib.pyplot as plt
import numpy as np

# Given data
data = {
    "calories": 2763.9,
    "carbohydrates": 320.0,
    "protein": 155.03,
    "fat": 87.19,
    "fiber": 11.06,
}

# Extract numerical values for each nutrient
values = np.array(list(data.values()))
labels = list(data.keys())

# Set up 3D bar chart
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Bar positions along the x-axis
xpos = np.arange(len(labels))

# Bar heights
ypos = np.zeros(len(labels))

# Bar widths
zpos = np.zeros(len(labels))

# Create 3D bars
bars = ax.bar(xpos, ypos, zpos, color='skyblue', zdir='y', alpha=0.7)

# Set labels for each axis
ax.set_xticks(xpos)
ax.set_xticklabels(labels)
ax.set_xlabel('Nutrient')

ax.set_yticks([0])
ax.set_yticklabels(['Amount'])
ax.set_ylabel('')

ax.set_zlabel('Value')
ax.set_title('3D Bar Chart - Nutrient Distribution')

# Add data labels on top of the bars
for bar, value in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2, 0, value, ha='center', va='bottom', color='black', fontweight='bold')

# Show the plot
plt.show()




