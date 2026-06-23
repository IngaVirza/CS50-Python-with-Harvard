def main():
    with open("alice.txt", "r") as f:
        contents = f.readlines()

    print(contents[0])    




main()
