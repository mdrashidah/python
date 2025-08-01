words = ["donkey", "Donkeys","animal","intelligent","life","Animals","herbivore"]

with open("donkey_replace.txt", "r") as f:
    content = f.read()


for word in words:
    content = content.replace(word,"#-#"*len(word) )
#we use "word" as variable in string because we want to replace all the words in the list 

with open("donkey_replace.txt", "w") as f:
    f.write(content)