name = input("What's your name?")


# file = open("name.txt", "w")
# file = open("name.txt", "a")
# file.write(f"{name}\n")
# file.close()


with open("names.txt", "a") as file:
    file.write(f"{name}\n")