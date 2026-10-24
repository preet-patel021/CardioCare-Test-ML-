def factorial(num):
    if(num == 1 or num ==0):
        return 1
    else:
        return(num*factorial(num-1))
print(factorial(4))


def fibonacci(n):
    if(n == 0):
        return 0
    if (n == 1):
        return 1
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
print(fibonacci(0))


#(//cheaking in for loop we use the if condition??)
for i in range(6):
    print(i)
    if i==4:
        break

else:
    print("sorry")


#(this is showing no error in this program becoaze here uesing try and except condition)
a =input("enter the number:")
try:
    for i in range(1,20):
        print(f"{int(a)} X {i}=={int(a)*i}")
except:
    print("invalid input!!")