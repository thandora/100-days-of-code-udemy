import pprint

# # Exercise:
# Using list comprehension, store the data that overlaps between the 2 files.
files_path = ["file1.txt", "file2.txt"]
lists = []
for file in files_path:
    with open(file) as f:
        lines = f.readlines()
        l = [int(x.strip()) for x in lines]
        lists.append(l)

list_1 = lists[0]
list_2 = lists[1]
result = [x for x in list_1 if x in list_2]

print(result)

# # Exercise
# Use dictionary comprehension to create a dictionary called result that
# takes each word in the given sentence and calculates the number of letters
# in each word.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above

result = {word: len(word) for word in sentence.split()}

pprint.pprint(result, sort_dicts=False)


# # Exercise
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# Don't change code above
weather_f = {day: (((9 / 5) * temp_c) + 32) for (day, temp_c) in weather_c.items()}
# Didn't add round() for readability.
pprint.pprint(weather_f, sort_dicts=False)
