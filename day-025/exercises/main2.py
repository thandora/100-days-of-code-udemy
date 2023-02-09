import pandas as pd

# pandas is usually shortened to pd
# and dataframe object as df
df = pd.read_csv("weather_data.csv")
print(df, "\n", "=" * 44)  # Seperator


# Selecting columns (or series in pandas) in a table (dataframe in pandas)
a = df["temp"]
# or
a = df.temp
# pandas make the 1st entry in the column as an attribute of the dataframe

# Average value over temp series (using mean method)
a = df["temp"].mean()

# Max value over temp series
a = df["temp"].max()

# Instead of accessing by using "keys" as you would in a dict, you
# can use the title of the series as an attribute to a pandas
# dataframe "condition" series.
a = df.temp

# Select rows where condition is met in column.
# i.e.
# select row where the value is a maximum at the temperature column
a = df[df.temp == df.temp.max()]

# Rows where temperature is less than 15
a = df[df.temp < 15]

# Convert Monday's temp to Fahrenheit
monday = df[df.day == "Monday"]
c_temp = float(monday.temp)
f_temp = (c_temp * 9 / 5) + 32

# Create a dataframe from scratch
my_dict = {
    "students": ["Aaron", "Balakay", "Denice"],
    "score": [90, 95, 92],
}

# Making DataFrame class of the dict
my_df = pd.DataFrame(my_dict)
# Convert to csv and save to a file
my_csv = my_df.to_csv("my_data.csv")
