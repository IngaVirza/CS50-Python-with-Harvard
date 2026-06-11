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


students_2 = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}

]

for student in students_2:
    print(student["name"], student["house"], student["patronus"], sep=", ")