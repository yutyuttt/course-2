students = ["Alissa", "Ben", "Charlie", "Dianna"]
grades = ["B", "D", "B", "A"]

key = "Charlie"

i = 0
found = False
while (not found) and (i < len(students)):
    if students[i] == key:
        found = True
    else:
        i += 1

if found:
    print(grades[i])
else:
    print(f"{key} not a student.")