class nikolay():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def person(self):
        if self.name != 'Николай':
            self.name = "Я не " + self.name+ ",a Николай"
        return(self.name)
person1 = nikolay('Иван', 31)
person2 = nikolay('Николай', 31)
print(person1.person())
print(person2.person())
