number = [2,1,3,5]
print(number)
print(number.append(4)) 
# yeah sbb mein none iss wajah sein aa rha tha kyuki 
#append(), sort(), reverse() → all change the list directly,
#but return None. they do not return a new list.
#So to deal with it Call first, then print. Not both together,: eg:line no. 10
print(number)
print(number.sort()) 
print(number)
number.reverse()
print(number)
number.append(6)
print(number)
number.insert(0, 0)  # insert at index 0
print(number)
number.remove(2)  # remove first occurrence of 2
print(number)
number.pop(3)  # remove particular element
print(number)
print(number.copy())  # copy the list
#print(number.copy(5))  # this will raise an error, as copy() does not take any arguments
print(number)
number.clear()  # clear the list
print(number)  # should print an empty list
print(number)