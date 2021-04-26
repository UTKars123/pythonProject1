# #n!=n*n-1*n-2*n-3*....
# #n!=n*n-1!
# def factorial_iterative(n):
#     fac=1
#     for i in range(n):
#         fac=fac*(i+1)
#     return fac
# number=int(input("Enter the number\n"))
# print("factorial using iterative method is ",factorial_iterative(number))

# #n!=n*n-1*n-2*n-3*....
# #n!=n*n-1!
# def factorial_recursive(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial_recursive(n-1)
#     # 5*factorial_recursive(4)
#     # 5*4*factorial_recursive(3)
#     # 5*4*3*factorial_recursive(2)
#     # 4*3*2*factorial_recursive(1)
#     # 5*4*3*2*1=120
# number=int(input("Enter the number\n"))
# print("factorial using recursive method is ",factorial_recursive(number))
while 1:
 def fibbnocci_recursive(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibbnocci_recursive(n-1)+fibbnocci_recursive(n-2)

 number=int(input("Enter the number\n"))
 print("factorial using recursive method is ",fibbnocci_recursive(number))

