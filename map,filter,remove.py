# numbers=["1","2","3"]
# # for i in range(len(numbers)):
# #     numbers[i]=int(numbers[i])
# numbers=list(map(int,numbers))
# numbers=numbers[2] +1
# print(numbers)


# lst=[1,2,3,4,5]
# def square(x):
#     return x*x
# sq=list(map(square,lst))
# print(sq)


# lst=[1,2,3,4,5]
# # sq=list(map(lambda x:x*x,lst))
# # print(sq)
# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
# func=[square,cube]
# for item in range(len(lst)):
#     print(list(map(lambda x:x(lst[item]),func)))

     #filter
# lst_1 = [1,2,3,4,5,6,7]
# def greater(num):
#     return num>5
# a=list(filter(greater,lst_1))
# print(a)


     #reduce
from functools import reduce
#list1=[1,2,3,4]
# num=0
# for i in list1:
#     num=i+num
# print(num)

list1=[1,2,3,4,5,6,7]
print(reduce(lambda x,y:x+y,list1))


