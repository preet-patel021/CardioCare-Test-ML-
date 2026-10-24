count = 5
while(count > 0):
    print(count)
    count = count - 1
else:
    print("counter is 0")

for i in range(12):
    if(i == 10):
        continue
    print("5 *", i,"=",5*i)