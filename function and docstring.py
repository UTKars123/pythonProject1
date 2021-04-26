"""
a=2
b=5
c=sum((a,b))
#builtin function
print(c)
"""
"""
def function1():
    print("hello world")
function1()
function1()
"""
def function2(a,b):
    """ This is a function which will calculate averager of two number
    this function does not work for three number"""
    c=(a+b)/2
    #print(c)
    return c           # return the value of c to the function2 and then v is print
v=function2(3,3)
print(v)
print(function2.__doc__)

