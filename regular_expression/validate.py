import re
email = input("What's your email?").strip()

# 1111111
# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")    

# 2222222
# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("Valid")
# else: 
#     print("Invalid")    

# 333333333


# if re.search(".+@.+", email):
# if re.search("..*@.*", email):
if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")    