
file = open('data.txt','r')
try:
    print(file.read())
finally:
    file.close()