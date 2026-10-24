# info = {"preet",19,False,9.5,19,False}
#print(info)
#t = {}
#print(type(t))
#for value in info:
 #   print(value) 


###s1 ={1,2,3,5,7,6}
#s2 ={8,4,6,9}
#print(s1.union(s2))
#print(s1.update(s2))
#print(s1,s2)
#s3 ={5,4,6,7}
#s4 ={1,5,6}
#print(s3.intersection(s4))
#print(s3.intersection_update(s4))

cities ={"tokoy","madrid","berlin","delhi"}
cities2={"seoul","kabul","delhi"}
cities3=cities.symmetric_difference(cities2)
print(cities3)
cities4=cities.symmetric_difference_update(cities2)
print(cities4)