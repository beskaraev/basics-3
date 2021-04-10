# 04/04/2021 Reading a file

# filepath = "C:\\dev\\2020-fall\\basics\\data\\students.txt"  # this is only for windows
filepath = "C:/dev/2020-fall/basics/data/students.txt"

# ============== READING FROM FILE ================
# Reading an Entire File
# with open(filepath) as students:
#     contents = students.read()
#     print(contents)

# Reading Line by Line
# with open(filepath) as students:
#     for line in students:
#         print(line, end='')


# Making a List of Lines from a File
# with open(filepath, 'r') as students:   # 'r' is an optional parameter for opening mode, r is default mode that open in READ ONLY mode
#     lines = students.readlines()
#
# print(lines)
# print(lines[0].strip())
# print(lines[-1])
# print("================")
# for line in lines:
#     print(line.strip())

# ============== READING FROM FILE ================
with open(filepath, 'a') as students:   # 'a' is for append , that appends the value to the file content, 'w' is for write, that truncates the file and adds new content
    print("writing to the file.. ")
    students.write(f"\nSergey")

with open(filepath, 'r') as students:
    lines = students.readlines()
    print(lines)
