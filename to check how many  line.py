#counting the no. of words

with open("data_filter.txt") as f :
    lines = f.readlines()

print("to check 'python' words are present in how many line is there in the file \n")

#count1 = line.count("python")
#count keyword is used to count the no. of words
#line represents each line(string) in the file
#lines represents all the lines in the file
#line_ represents the line number

line_ = 1
for line in lines:
    if ("python" in line):
        print(f"'python' word is present in line {line_}")
        #break has removed because we want to check all lines
    line_ += 1 
        

else:
    print("word python is not present in any line") # This line will always be executed
