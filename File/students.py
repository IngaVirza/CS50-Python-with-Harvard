
# with open("students.csv") as file:
#     for line in file:
#         # row = line.rstrip().split(",")
#         # print(f"{row[0]} is in {row[1]}")
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")

import csv
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)        


# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house":house}
#         students.append(student)

# def get_name(student):
#     return student["name"]


# for student in sorted(students, key=get_name, reverse=True): 
#     print(f"{student['name']} is in {student['house']}")


# with open("students.csv") as file:
    # for line in file:
    #     name, home = line.rstrip().split(",")
    #     student = {"name": name, "home":home}
    #     students.append(student)
    # reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name": name, "home": home})

# for student in sorted(students, key=lambda student: student["name"]): 
#     print(f"{student['name']} is from {student['home']}")



    
#     reader = csv.DictReader(file)
#     for row in reader:
#             students.append({"name": row["name"], "home": row["home"]})

    
# for student in sorted(students, key=lambda student: student["name"]): 
#     print(f"{student['name']} is from {student['home']}")


name = input("What's your name?")
home = input("Where's your home?")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])