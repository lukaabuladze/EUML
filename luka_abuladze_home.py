# a = int(input())
# b = int(input())
# c = int(input())
# print(max(a,b,c))


# import random
# for i in range(0,10):
# 	print(random. randint(0,22))


# def average(a,b):
# 	print((a+b)/2)
# average(5,10)


# def odd(a):
# 	if a % 2 == 0:
# 		print("even")
# 	else:
# 		print("odd")

# odd(8)			


# number = [1,2,3,4,5]
# print(min(number))
# print(max(number))
# print(sum(number))
# print(sum(number) / len(number))
# number.append(6)
# print(number)
# number[4] = 7
# print(number)
# number.remove(number[4])
# number.sort()
# print(number)

# numbers = [1,2,3,4,5,6,7,8,9]
# for i in numbers:
# 	if i % 2 != 0:
# 		numbers.remove(i)

# print(numbers)

# import random
# numbers = [1,2,3,4,5,6,7,8,9,10]
# random.shuffle(numbers)
# print(numbers)

# import collections
# c = collections.Counter([1, 5, 23, 5, 12, 2, 5, 1, 18, 5])
# a = c.most_common(1)
# print(a)

# lst = ['python', 'php pascal', 'javascript', 'java', 'c++']
# res = max(lst, key = len)
# print(res)

# import math
# x = round(5.898)
# y = math.ceil(1.13)
# d = math.floor(0.6)
# b = math.trunc(2.77)
# print(x,"   ",y,"   ",d,"   ",b)

# import math
# def Sqr(x):
# 	return math.sqrt(x)

# print(Sqr(225625))
# print(Sqr(4225))

# import random
# x = random.random()
# print(round(x,3))

# import random
# n = random.uniform(100, 120)
# print(round(n, 1))

# def Nam(a,b):
# 	return (a+b)/2
# print(Nam(2,3))
# print(Nam(6,1))
# print(Nam(6,9))

# def Cub(a):
# 	return a**3
# print(Cub(2))
# print(Cub(3))

# def Min(a,b):
# 	if a > b:
# 		print(b,"მინიმალურია")
# 	else:
# 		print(a,"მინიმალურია")

# Min(2,3)

# import math
# def Fact(a):
# 	print(math.factorial(a))
# Fact(8)

# def Hell():
# 	print("hello world")
# Hell()

# lst = []
# lst.append(input())
# lst.append(input())
# lst.append(input())
# lst.append(input())
# lst.append(input())
# lst.append(input())
# lst.append(input())
# lst.append(input())
# lst.append(input())
# lst.append(input())
# print(lst)

# lst = ["Banana","Watermelon","Apple"]
# lst.sort(reverse=True)
# print(lst)

# def Lst(num):
#   for x in num:
#     print(x**x)

# number = [1,2,3]
# Lst(number)

# lst = [1,2,3,4,5]
# x+10
# for x in lst:
# 	print(x)	
# print(lst)

# lst = [1,2,3,4,5]
# incremented_list = [x+10 for x in lst]
# print(incremented_list)


# def common_elements(list1, list2):
# 	 return list(set(list1) & set(list2))
# print(common_elements(list1=[7,8,1,6,5],list2=[3,2,5,10,9]))	

# lst1=[1,2,3,4,5]
# lst2=[3,2,5,10,9]
# def Common(a, b): 
#     result=False
#     for x in a: 
#         for y in b: 
#             if x==y: 
#                 result=True
#                 return result  
#     return result 

# print(Common(lst1,lst2))

# def remove_odd(lst):
#     for i in lst[:]:
#         if i % 2 != 0:
#             lst.remove(i)
#     return lst
# print(remove_odd([1,2,3]))
