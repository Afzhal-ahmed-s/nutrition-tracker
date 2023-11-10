from matplotlib import pyplot as plt

data = {
    "calories": "2763.9 kcal",
    "carbohydrates": "320.0 g",
    "cholesterol": "1631.0 mg",
    "fat": "87.19 g",
    "fiber": "11.06 g",
    "monounsaturated": "32.09 g",
    "polyunsaturated": "14.92 g",
    "potassium": "4182.32 mg",
    "protein": "155.03 g",
    "saturated": "32.33 g",
    "sodium": "1316.1 mg",
    "sugar": "68.16 g"
}

# Extract numerical values for carbs, protein, and fat
carbs = float(data.get("carbohydrates").split()[0])
protein = float(data.get("protein").split()[0])
fat = float(data.get("fat").split()[0])

# Total grams
total_grams = carbs + protein + fat

# Plotting
categories = ['Total Grams', 'Carbohydrates', 'Protein', 'Fat']
values = [total_grams, carbs, protein, fat]

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(categories, values, color=['lightgray', 'skyblue', 'lightgreen', 'lightcoral'])

# Adding data labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}', ha='center', va='bottom', color='black', fontweight='bold')

# Adjusting label positions and colors
ax.set_xlabel('Nutrient', color='grey', fontsize=12)
ax.set_ylabel('Amount (g)', color='grey', fontsize=12)
ax.set_title('Nutrient Distribution', color='grey', fontsize=16, pad=20)

# Adding a little space between the bars
plt.ylim(0, max(values) + 20)

# Removing x-axis ticks and adjusting y-axis ticks
ax.tick_params(axis='x', which='both', bottom=False)
ax.tick_params(axis='y', which='both', labelsize=10)

plt.show()