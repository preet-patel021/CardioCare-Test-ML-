info ={"name":"preet","age":20,"city":"surat"}
print(info)
print(info["name"])
print(info["age"])

#(//multiple value//)
print(info.values())
print(info.keys())
#for key in info.keys():
 #   print(info[key])
#for key, value in info.items():
 #   print(f"this is info of {key} is {value}")

 #(//update methode//)
info.update({"name2":"kinjal"})
print(info)
#info.clear()
#print(info)
info.pop("name2")
print(info)
del info["age"]
print(info)