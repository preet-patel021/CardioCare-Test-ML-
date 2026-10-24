import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
hour = time.strftime("%H")
print(hour)
minute = time.strftime("%M")
print(minute)
seconds = time.strftime("%S")
print(seconds)
if(hour >= 6 and hour <= 11):
    print("good morning")
elif(hour >= 12 and hour <= 17):
    print("good afternoon")
elif(hour >= 18 and hour <= 20):
    print("good evening")
else:
    print("good night")