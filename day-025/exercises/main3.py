import pandas as pd

# Task: create a csv with the counts of each
# of the primary fur color of squirrels

# All data
df = pd.read_csv("squirrel_central_park.csv")


colors = ["Gray", "Cinnamon", "Black"]
n_colors = {"Fur Color": [], "Count": []}

for color in colors:
    # Select all rows that matches queried color
    column = df[df["Primary Fur Color"] == color]
    # Count how many rows on query
    n = column.count(axis=0)["Primary Fur Color"]
    # Append to dictionary
    n_colors["Fur Color"].append(color)
    n_colors["Count"].append(n)

# Convert 
colors_csv = pd.DataFrame(n_colors).to_csv("colors.csv")
