# # lamda function is a one liner function
# minus=lambda x,y:x-y
# print(minus(9,4))   #without the use of function
#
#
# def minus(x,y):
#     return x-y
# print(minus(9,4))
#
#
#
# def a_first(a):
#     return a[1]
# a=[[1,14],[5,6],[8,23]]
# a.sort(key=a_first)
# print(a)

a=[[2,3],[3,2],[2,2]]
a.sort(key=lambda a:a[1])
print(a)

a=[[2,3],[3,2],[2,2]]
a.sort(key=lambda a:a[0])
print(a)