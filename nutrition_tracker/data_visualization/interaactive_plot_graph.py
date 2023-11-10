import plotly.express as px

# Given data
data = {
    "carbohydrates": 320.0,
    "protein": 155.03,
    "fat": 87.19,
    "fiber": 11.06,
}

# Extract numerical values for each nutrient
values = list(data.values())
labels = list(data.keys())

# Create a DataFrame for Plotly
df = {"Nutrient": labels, "Amount": values}
fig = px.bar(df, x="Nutrient", y="Amount", title="Nutrient Distribution")

# Add data labels on top of the bars
fig.update_traces(texttemplate='%{y:.2f}', textposition='outside')

# Show the plot
fig.show()