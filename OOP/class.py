class User:
    def __init__(self, name, age):
    
        self.name = name
        self.age = age
        self.is_human = True

user1 = User("Kirill",18) #Экземпляр
user2 = User("Alexander", 32)

print(user1.__dict__)