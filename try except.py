print("enter number 1")
number1=input()
print("enter number 2")
number2=input()
try:
 print("the sum of two number is ",int(number1)+int(number2))
except Exception as e:
    print(e)

print("this is important line")