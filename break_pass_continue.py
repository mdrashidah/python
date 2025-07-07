#break, pass, continue
#example of break and continue statement in while loop
lt = ["ali","omar",1,2,3,4,5,6]
i = 0
while i<len(lt):
    if lt[i] == 3:
        i+=1
        continue
    if lt[i] == 5:
        break
    print(lt[i])
    i+=1

#example of break and continue statement in for loop
lt = ["ali","omar",1,2,3,4,5,6]
for i in lt:
    if i == 3:
        continue
    if i == 5:
        break
    print(i)

#example of pass statement
lt = [1,2,3,4,5,6]
for i in lt:
    if i == 2:
        pass
    #print(i)