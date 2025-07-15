#q1
list = ["ali","amr","omar","ahmed","sohel"]
for i in list:
    if(i.startswith("a")):
        print(f"hello {i}")
    if (i.endswith("r")):
        print(f"goodbye {i}")
    
        pass
for num in range(5):
    pass
print("------------------------")
#q2
i=0
num = int(input("Enter a multiplicant number: "))
while(i < 11):
    print(f"{num} * {i} = {num * i}")
    i += 1
# i+= 1 is used becaus ewe have to handle the increment manually in a while loop
print("------------------------")
#q3
num = int(input("Enter a multiplicant number: "))
for i in range(0, 11):
    print(f"{num} * {i} = {num * i}")
    # i += 1
# i+= 1 is not used in for loop, it is automatically handled by the for loop
print("------------------------")
#q4
print("Enter a number to check if it is prime or not")
num = int(input("Enter a number: "))
for i in range (2, num):
    if(num%i) == 0:
        print(f"{num} is not a prime number")
        break
    else:
        print(f"{num} is a prime number")
        break
print("------------------------")
#q5
print("enter the no. to check the the sum of first n natural numbers")
num = int(input("Enter a number: "))
sum = 0
#we have take sum as 0 because we have have to add it to the first n natural numbers
i =1
while(i <= num+1):
    sum += i
# sum = sum + i
    i += 1
#i+= 1 is used to increment the value of i by 1 in each iteration
print(f"The sum of first {num} natural numbers is {sum}")
print("------------------------")
#q6 (to print factorial of a number)
print("Enter a number to check the factorial")
print("------------------------")
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print(f"The factorial of {num} is {fact}")
print("------------------------")
#q7 (to print fibonacci series)
print("Enter a number to print fibonacci series")
num = int(input("Enter a number: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(num):
    print(a, end=" ")
    a, b = b, a + b
print()  # for a new line after the series
print("------------------------")
#q8 to check prime no. or not in a while loop
print("Enter a number to check if it is prime or not")
num = int(input("Enter a number: "))
i = 2
while i<=num :
    if (i%num == 0):
        print("not a prime no.")
        break
    else:
        print("prime")
        break
        i+=1
print("------------------------")
#q9 to print stars patterns 
