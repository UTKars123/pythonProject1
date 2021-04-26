#task to make faulty calculator
#45*3=555,56+9=77,56/6=4
d=["+","-","*","/"]
d1=int(input("enter the value of d1\n"))
d2=int(input("enter the value of d2\n"))
d3=input("enter the symbol of addition,substraction,multiplication,division:\n")
if d3 in d[0]:
    if d1==56 and d2==9:
        print("77")
    else:
        print("addition of d1 and d2 is ",d1+d2)
elif d3 in d[1]:
 print("substraction of d1 and d2 is ",d1 - d2)
elif d3 in d[2]:
    if d1==45 and d2==3:
        print("555")
    else:
        print("multiplication of d1 and d2 is ", d1 * d2)
else:
    if d1==56 and d2==6:
        print("4")
    else:
        print("division of d1 and d2 is ",d1 / d2)


