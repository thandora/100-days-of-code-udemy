import pandas as pd

# Task: create a csv with the counts of each
# of the primary fur color of squirrels

# All data
data = pd.read_csv("squirrel_central_park.csv")

colors = ["Gray", "Cinnamon", "Black"]
n_colors = {"Fur Color": [], "Count": []}

for color in colors:
    # Select all rows that matches queried color
    column = data[data["Primary Fur Color"] == color]

    n = len(column)
    # or by use of count method
    # Count how many rows on query
    n_2 = column.count(axis=0)["Primary Fur Color"]

    # Append to dictionary
    n_colors["Fur Color"].append(color)
    n_colors["Count"].append(n)

# Convert
colors_csv = pd.DataFrame(n_colors).to_csv("colors.csv")
