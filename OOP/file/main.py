
file = open('data.txt','r')
# try:
#     print(file.read())
# finally:
#     file.close()


# Better

with open('data.txt', 'r') as file:
    print(file.read())

class FileOpener:
    def __init__(self, file_path: str, mode:str):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        file = open(self.file_path, self.mode)
        return file

    def __exit__(self):
        pass

file_opener = FileOpener('data.txt','r')

with FileOpener('data.txt', 'r') as file:
    print(file.read())
