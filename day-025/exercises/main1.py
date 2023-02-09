import pprint
import csv
import pandas as pd

# # 1. Using std lib
# with open ("weather_data.csv", "r") as data_file:
#     data = data_file.readlines()
#     print(data)

# # 2. Using csv module
# # mode is default to "r"
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(float(row[1]))
#     print(temperatures)

# # 3. Using pandas package
# data = pd.read_csv("weather_data.csv")
# print(data["temp"])

