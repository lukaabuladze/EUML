# # დავალება 1
# f = open("write.txt", "w")
# f.write("24, 39, -90")
# f.close()

# დავალება 2
# f = open("write.txt", "w")
# for i in range(0,100):
# 	s = str(i)
# 	f.write(s)
# f.close()

# დავალება 3
# for x in range(1,30):
# 	f = open("myFiles"+str(x), 'w')
# 	f.write("Programmer")
# 	f.close()

# დავალება 4
# import os
# filename = "myfiles"
# os.makedirs(filename)

# დავალება 16
# lst1= {"green", "blue"}
# lst2= {"blue", "yellow"}
# print(set.union(lst1, lst2))
# print((lst1|lst2))
# print(set.intersection(lst1, lst2))
# print((lst1&lst2))
# print(set.difference(lst1, lst2))
# print((lst1-lst2))
# print(set.symmetric_difference(lst1, lst2))
# print((lst1^lst2))

# # დავალება 17
# lst={100,77,344,10,45}
# print(max(lst))
# print(min(lst))

# დავალება 11
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {**dic1 , **dic2, **dic3}
# print(dic4)
# დავალება 12
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# if 2 in d:
# 	print("არსებობს")
# else:
# 	print("არ არსებობს")
# დავალება 13
# d = {'x': 10, 'y': 20, 'z': 30}
# for i in d:
# 	print(i,d[i])