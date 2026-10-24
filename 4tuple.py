tup = (1,2,3,"Preet",4,5,True,1,1)
print(tup)
print(tup[3])
print(tup[1])
if "Preet" in tup:
    print("yes preet is present in tup")
else:
    print("no preet is not present in tup")
x = len(tup)
print(x)
result = tup.count(1)
result1 = tup.index(1,4,8)
print(result)
print(result1)