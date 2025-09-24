a = [1, 2, 3, 4, 5]
print(a)
print(type(a))
a[0]=1   
print(a)

print("S===========Slicing===========")
print(a[1]) #2
print(a[-1]) #5
print(a[0:3]) # 1,2,3
print(a[2:]) #3,4,5
print(a[:3]) # 1,2,3
print("-----------------------------")
a = [1, True, 'Ram', 2.5, [1, 2, 3, 4]]
print(a)
print(type(a))
print(list(range(20)))
print(type(a))
print(a[0], " type is ", type(a[0]))
print(a[1], " type is ", type(a[1]))
print(a[2], " type is ", type(a[2]))
print(a[3], " type is ", type(a[3]))
print(a[4], " type is ", type(a[4]))
print(a[4][1])
print("-----------------------------")
names = ["Ram"]
print(names)
names.append("Sam")
names.append("Ravi")
names.append("Kumar")
print(names)
name2 = ["Sara", "Anitha"]
names.extend(name2)
print(names)
names.insert(0,"Suriya")
print(names)
print("-----------------------------")