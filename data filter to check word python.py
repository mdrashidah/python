with open("data_filter.txt") as f :
    content = f.read()

print("to check wheather the file contain the word python \n")

count1 = content.count("python")
#count keyword is used to count the no. of words
if "python" in content:
    print("word python is present")
if count1 > 0:
    print(f"'python' word is present {count1} times")
else:
    print("word python is not present")