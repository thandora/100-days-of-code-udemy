# Exercise:
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
