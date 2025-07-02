# File: python/sets.py
collections0 = {1,2,3,4,5}
print(type(collections0))
print(collections0)

collections = {} # This is an empty dictionary, not a set
print(type(collections))
print(collections)

collections2 = set()  # This is an empty set
print(type(collections2))
print(collections2)

# Adding elements to an empty set
print("\n--- Adding elements to collections2 ---")
collections2.add(10)
print("After adding 10:", collections2)
collections2.add(20)
print("After adding 20:", collections2)

collections2.update([30, 40, 50])
print("After updating with [30, 40, 50]:", collections2)

collections2.update({60, 70}, [80, 90])
print("After updating with {60, 70} and [80, 90]:", collections2)
