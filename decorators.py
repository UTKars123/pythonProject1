# def function1():
#     print("Welcome Now")
# function2=function1  #()-this bracket calls the function
# del function1
# function2()

# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# a=funcret(1)
# print(a)

# def executor(func):
#     func("this")
# executor(print)

#function kea anderfunction hum daaal sakte hai as an argument
# or hum function dwara function function ko return bhi kar sakte hai

#decorators concept
def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("executed")
    return nowexec
@dec1
def who_is_happy():
    print("i am happy")
# who_is_happy=dec1(who_is_happy)
who_is_happy()

