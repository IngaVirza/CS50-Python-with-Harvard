# Ask user for their name
name1 = input("What's your name?")

#Remove whitespace from str
name1 = name1.strip()

# Capitalize user's name
name1 = name1.capitalize()

# Capitalize user's name
name1 = name1.title()

# Remove whitespace from str and capitalize user's name short code 
name = input("What's your name?").strip().title()
# Say hello to user
print(f"hello, {name}")