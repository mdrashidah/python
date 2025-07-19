# ------Recursion-------
# Reading the file in the function
f = open("file.txt", "r")
data = f.read()
print(data)
f.close()

# write in the file in the i/o function
new_hadith = " hello india this is rashid"

f = open("hadith2.txt", "w")
f.write(new_hadith)
f.close()

# readline by line method
f = open("file.txt")
hello1 = f.readline()
print(hello1, type(hello1))

hello2 = f.readline()
print(hello2, type(hello2))

hello3 = f.readline()
print(hello3, type(hello3))
f.close()

# opening of a image file
# b = open("r.jpeg", "rb") 
# he=b.read()
# print(he)
# b.close()

# Reading the file's specific no.of characters
y = open("file.txt", "r")
#data = y.read(11)
print(y.read(11))
f.close()

#print using while loop
f = open("hadith3.txt")
line = f.readline()
while (line != ""):
    print(line)
    line = f.readline()
    #agar yahi prr main likh deta huu ki " f = open("hadith3.txt") " toh yeah ek infinite loop ban jaata haa jo continue open krrke print krte jaaega
f.close()

# append mode means line add hote jaaega
b = "baarakallahu feekum"
f = open("hadith3.txt", "a")
f.write(b)
f.close()
# mae jitne baar run krunga utne baar "baarakallahu feekum" add hota jaaega