def main():
    name = input("What is your name?")
    hello(name)

def hello(to='world'):
    print("hello,", to)


main()


def main2():
    x = int(input("What's x?"))
    print("x squared id", square(x))


def square(n):
    return n ** 2

main2()    
