# name = input("What's your name?")


# file = open("name.txt", "w")
# file = open("name.txt", "a")
# file.write(f"{name}\n")
# file.close()


# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")




# with open("names.txt", "r") as file:
#     # lines = file.readlines()

#     for line in file:
#         print("hello,", line.rstrip())    



# names = []

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"hello, {name}")        


with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())        