# l=4 #global variable  #global scope tak hai
# print(l)
# def function1():
#     #l=2  #local variable#first check variable in local space
#     m=4
#     global l # it have permissions to change the global variable everywhere
#     l=l+45
#     print(l)
# function1()
# print(l)
# #print(m)   # m is not found in global variable

def harry():
    x=20
    def rohan():
        global x
        x=44
    print("before calling rohan",x)
    rohan()
    print("after calling rohan",x) #x is value of harry local file
harry()
print(x)