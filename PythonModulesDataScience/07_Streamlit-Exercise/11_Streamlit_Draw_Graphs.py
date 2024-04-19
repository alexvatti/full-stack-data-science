import streamlit as st

#  Use Python's import statement to load modules 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#file_path=r"iris_dataset.csv"
#iris_df=pd.read_csv(file_path)
url = "https://raw.githubusercontent.com/alexvatti/full-stack-data-science/main/PythonModulesDataScience/07_Streamlit-Exercise/iris_dataset.csv"

# Read the CSV file into a DataFrame
iris_df = pd.read_csv(url)

# Display the DataFrame
print(iris_df.head())
iris_df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species_labels','species']

st.header("Iris Visualization")
# Extract the values and index from value counts
value_counts = iris_df["species"].value_counts()
values = value_counts.values
labels = value_counts.index
cat_name="species"
fig, axs = plt.subplots(1, 2, figsize=(8, 6))  # 1 row, 2 columns
# Create a bar graph
axs[0].bar(labels, values)
axs[0].set_title(f'Frequency of {cat_name}')
axs[0].set_xlabel('Categories')  # Set x-label
axs[0].set_ylabel('Count')       # Set y-label

axs[1].pie(value_counts.values, labels=value_counts.index, autopct='%1.1f%%', startangle=140)
axs[1].set_title(f'Relative Frequency of {cat_name}')
plt.tight_layout()
st.pyplot(fig)

for con_var in ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']:
    fig, axes = plt.subplots(1, 2, figsize=(8, 6), gridspec_kw={'width_ratios': [3, 2]})

    # Plot histogram without KDE on the left
    axes[0].hist(iris_df[con_var], color='skyblue', edgecolor='black')
    axes[0].set_xlabel('Value')
    axes[0].set_ylabel('Frequency')
    axes[0].set_title(f'Histogram {con_var}')

    # Plot histogram with KDE on the right
    sns.histplot(data=iris_df, x=con_var, kde=True, color='orange', edgecolor='black', ax=axes[1])
    axes[1].set_xlabel('Value')
    axes[1].set_ylabel('Density')
    axes[1].set_title('Histogram with KDE')

    # Adjust layout
    plt.tight_layout()
    st.pyplot(fig)

sns.set_style("whitegrid")
output_var="species"
fig, axes = plt.subplots(2, 2, figsize=(8, 6))
fig.suptitle('Box-Plots Features Vs  Flower Type')
cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
k=0
for i in range(2):
    for j in range(2):
        sns.boxplot(ax=axes[i, j], x=output_var, y=cols[k], data=iris_df)
        k=k+1
st.pyplot(fig)


sns.set_style("whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(8, 6))
fig.suptitle('Kde-Plots')
k=0
for i in range(2):
    for j in range(2):
        sns.histplot(ax=axes[i, j], hue=output_var, x=cols[k], data=iris_df,kde=True)
        k=k+1
st.pyplot(fig)


fig, ax = plt.subplots(figsize=(8, 6))

# Plot heatmap
sns.heatmap(iris_df.corr(numeric_only=True), cmap="YlGnBu", annot=True, ax=ax)

# Set title and labels
ax.set_title('Correlation Matrix of Iris Dataset')

st.pyplot(fig)