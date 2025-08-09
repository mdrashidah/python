#example  of object attributes in Python

class Employee:
    language = "python"
    age = 19
    salary = 1000000
    def heat (self):
        print(f"Hello {self.name}, welcome to the {self.language} programming world!")
    def xyz (abc):
        print(f"salary is {abc.salary} and age is {abc.age}")
rashid = Employee()
rashid.name = "Rashid"
rashid.language = "SQL"
rashid.heat()
rashid.xyz()
