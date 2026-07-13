students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Gryffindor"},
]

gryffindors = [
    student["name"] for student in students if student ["house"] == "Gryffindor"
]