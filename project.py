#project 1
import time

timestamp = time.strftime("%H:%M:%S")
print(timestamp)

hour = int(time.strftime("%H"))
print(hour)

minute = time.strftime("%M")
print(minute)

second = time.strftime("%S")
print(second)

if hour >= 6 and hour <= 11:
    print("Good Morning")

elif hour >= 12 and hour <= 17:
    print("Good Afternoon")

elif hour >= 18 and hour <= 20:
    print("Good Evening")

else:
    print("Good Night")



#project 2
name = input("what is your name: ")
print("good morining")
print("aap ka swagt hai kon banega karodpati mein.")
question = ["what is capital in india? \n","how many color in india flg? \n","how many state in linda? \n","what is value of G in mathematic? \n"]
answer = ["delhi","3","28","9.8"]
a = 10000
b = 20000
c = 30000
d = 40000
answer1 = input(question[0])
if answer1.lower() == answer[0]:
    print("correct answer.you have won",a,"inr")
else:
    print("wrong answer.you take home amount is",0,"inr")
    exit()

answer2 = input(question[1])
if answer2 == answer[1]:
    print("correct answer.you have won",b,"inr")
else:
    print("wrong answer.you take home amount is",a,"inr")
    exit()

answer3 = input(question[2])
if answer3 == answer[2]:
    print("correct answer.you have won",c,"inr")
else:
    print("wrong answer.you take home amount is",b,"inr")
    exit()

answer4 = input(question[3])
if answer4 == answer[3]:
    print("correct answer.you have won",d,"inr")
else:
    print("wrong answer.you take home amount is",c,"inr")
    exit()
print("thank you for coming")
