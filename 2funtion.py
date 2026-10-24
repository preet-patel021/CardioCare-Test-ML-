def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
a = 8
b = 9
calculateGmean(a,b)
def average(a,b,c=2):
    print("the average is" , (a+b+c)/2)
average(8,3)





def average(*number):
    sum = 0
    for i in number:
        sum = sum + i
        print("the average is",len(number))
average(5,10)