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

# Number of variables
num_vars = len(labels)

# Compute angle of each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is circular, so we need to close the plot loop by repeating the first data point
values = np.concatenate((values, [values[0]]))
angles += angles[:1]

# Plot
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='skyblue', alpha=0.25)

# Set labels for each axis
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

# Display the plot
plt.show()