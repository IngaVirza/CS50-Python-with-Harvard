class Developer:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} write code")


class Designer:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} create interface")    


developer = Developer("Inga", 32)
developer.work()

designer = Designer("Max", 38)
designer.work