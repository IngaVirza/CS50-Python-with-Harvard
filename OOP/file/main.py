
file = open('data.txt','r')
# try:
#     print(file.read())
# finally:
#     file.close()


# Better

with open('data.txt', 'r'):
    print(file.read())