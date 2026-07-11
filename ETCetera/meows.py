# MEOWS =3
# for _ in range(MEOWS):
#     print("meow")

# class Cat:
#     MEOWS = 3


#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("meow")


# cat = Cat()
# cat.meow()


# def meow(n: int) -> str:
#     return "meow\n" * n

# number: int = int(input("Number: ")   )  
# meows: str = meow(number)
# print(meows, end="")


# import sys

# if len(sys.argv) == 1:
#     print("meow")

# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")    
# else:
#     print("usage: meows.py")    


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", help="Number of times to meow")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")