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
print(student["courses"])
print(student)
print(list(student.keys()))  
print(tuple(student.keys()))

print(student.get("xyz"))