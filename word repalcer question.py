word = "donkey"
words = "Donkeys"

with open("donkey_replace.txt","r") as f:
    content = f.read()

content_ = content.replace(word,"******")
content_ = content.replace(words,"******")

with open("donkey_replace.txt","w") as f:
    f.write(content_)