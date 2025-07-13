print("Multiplication Table Generator")
print("This program generates a multiplication table for a given number from 0 to 10.")
# Get the multiplier number from the user
num = int(input("Enter a multiplier number: "))
for i in range(0, 11):
    print(f"{num} * {i} = {num * i}")


print("This program generates a reverse multiplication table for a given number from 0 to 10.")
# Get the reverse multiplier number from the user
num = int(input("Enter a multiplicant number: "))
for i in range(10,-1,-1):
    print(f"{num} * {i} = {num * i}")

