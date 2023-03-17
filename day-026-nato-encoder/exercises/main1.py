import random
import pprint

# List comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# Generate list of random grade for each name in names using list comprehension
grade_book = {student: random.randint(80, 100) for student in names}
# Generate list of names of students and their grades whos score is above 90
passed_students = {
    student: grade for (student, grade) in grade_book.items() if grade > 90
}
pprint.pprint(grade_book)
pprint.pprint(passed_students)
