import pandas as pd

student_dict = {
    "student": ["Christian", "Klint", "Labadia"],
    "score": [85, 80, 90],
}

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

# Looping through data frame
for (index, row) in student_data_frame.iterrows():
    print(row["score"])