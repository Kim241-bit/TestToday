# loading the data in Python
import pandas as pd

df = pd.read_excel("E:/Documents/01. AWP 2024_25/Training/AirQualityUCI.xlsx", engine="openpyxl")
print(df.head())