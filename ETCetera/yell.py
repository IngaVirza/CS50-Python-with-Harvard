def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercase = map(str.upper, words)
    print(*uppercase)    


if __name__ == "__main__":
    main()

