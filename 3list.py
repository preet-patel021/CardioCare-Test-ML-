list1 = [1,2,3,4,5,6]
list2 = ["red","green","yellow"]
list3 = [1,"preet",3.5,True]
print(list1)
print(list2)
print(list3)
print(list2[0])
print(list2[1])
print(list2[2])
print(list2[len(list2)-1])
print(list2[-2])



animal = ["dog","cat","bat","mouse","pig","horse","donkey","goat","cow",]
print(animal[:])
print(animal[3:7])
print(animal[-7:-2])
print(animal[1:8:2])
print(animal[-8:-2:3])

list = [i*i for i in range(10)]
print(list)
list1 = [i*i for i in range(10) if i%2==0]
print(list1)

list = [1,45,89,3,46,12,4,3]
color = ["voilet","red","blue","green"]
list.sort()
print(list)
color.sort()
print(color)
print(list + color)