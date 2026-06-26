import re

def main():
    code = input("Hexadenical color code: ")
    pattern = r"^#[abcdefABCDEF0123456789]{6}$"
    match = re.search(pattern, code)
    if match: 
        print(f"Valid. Matched with {match.group()}")
    else: 
        print("Invalid.")    
main()    
    