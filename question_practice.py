condition = not False and False
print(condition)

condition1 = not False and False or True
print(condition1)

condition3 = not False
print(condition3)

condition4 = not False and False or True and not False
print(condition4)

d = 5 != 6
print(d) 

d = 5 == 6
print(d)


a = int(input("Enter a number: "))
a += 1
print(a)

a = int (input("Enter a number: "))
#a += 1
print(a)
b = int(input("Enter another number: "))
#b += 1
print(b)
print (a>=b)

#area of a square
a = int(input("enter the side of the square:   "))
area = a * a
print("Area of the square is: ", area)