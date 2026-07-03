class User:
    def __init__(self, name, age):
    
        self.name = name
        self.age = age
        self.is_human = True

    def say_hello(self):
        print(f"Hello, I'm {self.name}")


user1 = User("Kirill",18) #Экземпляр
user2 = User("Alexander", 32)

user1.say_hello()

print(user1.__dict__)