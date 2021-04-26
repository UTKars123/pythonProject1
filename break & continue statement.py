"""i=0
while(1):
 if i<5:
  i=i+1
  continue
 print(i+1,end=" ")
 if i==50:
  break
 i=i+1
 """
#quiz if input is greater than 100 then print congratulation
#otherwise take input again and again(input<100) using continue
while(1):
  i = int(input("enter the number\n"))
  if i>= 100:
   print("congratulation you have entered more than 100")
   break
  else:
   print("try again")
   continue





