d=["+","-","*","/"]
d1=int(input("enter the value of d1\n"))
d2=int(input("enter the value of d2\n"))
d3=input("enter the symbol of addition,substraction,multiplication,division:\n")
if d3 in d[0]:
 print("addition of d1 and d2 is ",d1+d2)
elif d3 in d[1]:
 print("substraction of d1 and d2 is ",d1 - d2)
elif d3 in d[2]:
   print("multiplication of d1 and d2 is ", d1 * d2)
else:
    print("division of d1 and d2 is ",d1 / d2)