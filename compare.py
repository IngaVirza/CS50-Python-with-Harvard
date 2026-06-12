x = int(input("What's x?"))
y = int(input("What's y?"))


if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")


else:
    print("x is equal to y")        



z = int(input("What's z?"))
q = int(input("What's q?"))


if z < q or z > q:
    print("z is not equal to q")

else:
    print("z is equal to q")

# better code 

i = int(input("What is i?"))
r = int(input("What's r?"))

if i != r:
    print("i is not equal to r")

else:
    print("i is equal to r")
