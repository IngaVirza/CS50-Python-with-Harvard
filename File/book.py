def main():
    with open("alice.txt", "r") as f:
        contents = f.readlines()

    chapter1 = contents[7:10]  
    
    with open("chapter1.txt", "w") as f:
        # f.write("Chapter I.")
        f.writelines(chapter1)




main()
