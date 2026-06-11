students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)


for i in range(len(students)):
    print(i + 1, students[i])



# dictionary


students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Rone": "Gryffindor",
    "Draco": "Slytherin",
}


for student in students:
    print(student, students[student], sep=", ")