collections0 = {1,2,3,4,5}
#print(type(collections0))
print(collections0)
collections0.add(6)
collections0.remove(2)
print(collections0)
collections0.update([7, 8]) # Adding multiple elements


print(collections0.pop())
print(collections0)

#the results it will give us weill :
# 1. Print the type of collections0, which is a set.
#{1,2,3,4,5}
# 2. print the elements of the collections0.pop() : any random elements eg. 1
# 3. Print the remaining elements in collections0 after popping one element.; eg. {2,3,4,5}
collections0.clear()
print(collections0)