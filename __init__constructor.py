class Employee:
    #rashid.name = "Rashid"
    language = "python"
    age = 19
    salary = 1000000
    def heat (self):
        print(f"Hello {self.name}, welcome to the {self.language} programming world!")
    def __init__ (abc):
        print(f"salary is {abc.salary} and age is {abc.age}")
rashid = Employee()
rashid.name = "Rashid"
#age = 21
#rashid.language = "SQL"
rashid.heat()
#rashid.xyz()


#__init__ is a constructor in Python that is called when an object is created from a class. It allows the class to initialize the attributes of the class.

# The __init__ method is a special method that is automatically called when a new instance of the class is created. It can take parameters to initialize the attributes of the class instance. In this case, it prints the salary and age of the employee when an instance is created.

# The __init__ method is defined with the first parameter as 'self', which refers to the instance being created. The 'self' parameter allows access to the attributes and methods of the class instance. In this example, 'abc' is used as an alternative name for 'self', but it is common to use 'self' for clarity.

# The 'heat' method is a regular method that prints a welcome message using the 'name