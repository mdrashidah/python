student = {
    "name" : "Rashid",
    "id" : 12345,
    "age" : 20, 
    "courses" : {
        "math" : 90,
        "english" : 85,
        "science" : 88
    }
}
print(student)
#print(list(student.keys()))  
#print(tuple(student.keys())) 

print(student.keys())  # Returns a view object of the keys

print(student.get("xyz")) # Returns None if key not found 
#print(student("xyz")) # Raises KeyError if key not found

