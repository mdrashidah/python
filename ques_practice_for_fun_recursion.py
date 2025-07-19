#greatest of three no.
def greatest():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    n3 = int(input("Enter third number: "))
    if n1 >= n2 and n1 >= n3:
        print(f"{n1} is the greatest number")
    elif n2 >= n1 and n2 >= n3:
        print(f"{n2} is the greatest number")
    else:
        print(f"{n3} is the greatest number")
greatest()
greatest()

#q2 preventing for a new line
print("a")
print("b",end="")
print("c",end="")
print("")

#q3 printing first 10 natural numbers using recursion
def n_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + n_natural_numbers(n - 1)
print(n_natural_numbers(10))

#q4 printing pattern using recursion
''' at n = 3
***
**
*
'''
def pattern(n):
    if n == 0:
        return
    else:
        print("*" * n)
        pattern(n - 1)
pattern(3)
pattern(5)

#q5
def ab():
    inch = int(input("Enter inches: "))
    cm = inch * 2.54
    print(f"{inch} inches is equal to {round(cm,2)} cm")
    print(f"{inch} inches is equal to {round(cm,2)} cm")
ab()
ab()
# or can also be done like this
def itc(inch):
    return inch * 2.54

n = int(input("Enter value in inches: ")) # this is used when we have to take input from user
print(f"{n} inches is equal to {round(itc(n),2)} cm")
n = itc(5)  # these are used when we have input already
print(f"The corresponding value in cms is {round(itc(n), 2)} cm")  # rounding off to 2 decimal places

#q6 to print the multiply table of a number using recursion
def mul(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
        
n = int(input("Enter a number to print its multiplication table: "))
mul(n)

#q7
