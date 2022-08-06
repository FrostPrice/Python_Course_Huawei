#%%

import requests as req
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

# Request data from website
html = req.get("https://www.worldometers.info/coronavirus")

# Check downloaded content
print(html.content)

# Parse HTML with BeautifulSoup
html_parsed = BeautifulSoup(html.content)

# Search for the required table
table = html_parsed.find("table", attrs={"id": "main_table_countries_today"})

# Check the table
print(table)

# Get all the rows
rows = table.find_all("tr")

# Check the first row
print(rows[0])

# Remove the HTML tags with the text.strip() method
print(rows[0].text.strip())

# Separate the string using a common devider
print(rows[9].text.strip().split("\n"))

# Store rows into a list (data)
data = []
for x in rows:
    data.append(x.text.strip().split("\n")[1:5])  # Get only the first 9 columns

# Convert the list into a dataframe
df = pd.DataFrame(data)

# Check the dataframe
print(df.head())

# Set the first rowas the header, and remove the second row
df = pd.DataFrame(data[9:], columns=data[0])

# Check the DataFrame
print(df.head())

# Save as a csv file
df.to_csv("covid19.csv")

# Get the required columns
df_plot = df[["Country,Other", "TotalCases"]]

# Get first 10 rows
df_plot = df_plot[:10]

# Check the dataframe
print(df_plot.head())

# Remove commas in digits, and convert string to int
df_plot["TotalCases"] = (
    df_plot["TotalCases"].apply(lambda x: x.replace(",", "")).astype(int)
)

# Check the dataframe
print(df_plot.head())

# Plot (Create the graph)
plt = df_plot.plot(kind="bar", x="Country,Other", y="TotalCases")
print(plt)

# %%
