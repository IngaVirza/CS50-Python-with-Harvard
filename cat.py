i = 0 
while i < 3:
    print("meowW")
    i += 1



for _ in range(3):
    print("hi")


while True:
    n = int(input("What's n?"))
    if n > 0:
        break

for _ in range(n):
    print("meowWW")


def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n?"))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow2")


main()    
