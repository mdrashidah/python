# function
def add(): #function definition
    a = int(input("Enter a number 'a': "))
    b = int(input("Enter a number 'b': "))
    print(a + b)
add() #function call
add()
print("Hello World")
add()
#function with arguments
#1.
def goodDay(name, ending):
    print("Good Day, " + name)
    #we can also use these things
    #print("Good Day, {name}" )
    #print(""Good Day,",name)
    print(ending)
    return "ok helo"

a = goodDay("ali", "Thank you") #"Harry", "Thank you" these are the arguments
a = goodDay("rashid", "Thank you")  #function call
print(a)
#2.
def greet (name):
    af = "hello "+ name
    return af
a = greet("rashid bro")
b = greet("omar bro")
print(a)
print(b)

#3.
def xyz(name ="haider"):
    print("Hello " + name)
xyz()
xyz("rashid")


