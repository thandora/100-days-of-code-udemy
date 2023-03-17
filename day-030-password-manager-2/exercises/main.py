"""
Exercise on exception handling
"""

# # FileNotFound
# with open("a_file.txt") as f:
#     f.read()

# # try:
#     f = open("non_existent_file.txt")
#     a_dict = {"a_key": "a_value"}
#     # b_value = a_dict["b_key"]
#     print("I am try.")

# except FileNotFoundError:
#     open("non_existent_file.txt", "w")
#     print("I am except. I run if exception FileNotFoundError is raised.")

# # Except block with error message.
# except KeyError as err_message:
#     print(f"{err_message} key is not in dictionary")
#     print("I am except. I run if KeyError is raised.")
# except TypeError:
#     print("????")
# else:
#     print("I am else. I will run if there were no exceptions ")

# finally:
#     print("I am finally. I always run")

# # KeyError
# a_dict = {"a_key": "a_value"}
# a_value = a_dict["b_key"]
# a_key

# # IndexError
# a_list = ["foo", "bar"]
# a_value = a_list[3]

# # TypeError
# a_text = "foo bar"
# a_number = 42
# print(a_text + a_number)

# # Raising an exception
height = float(input("Height (m): "))
weight = int(input("Weight: (kg): "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / (height**2)
print(round(bmi, 2))
