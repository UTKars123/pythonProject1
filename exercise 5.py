# Health Management System

def getdate():
    import datetime
    return datetime.datetime.now()

while 1:
 b=int(input("press 1 to  lock the data\n""press 2 to retrieve the diet\n"))
 if b==2:
  print("for harry Press 1,for hamad Press 2,for rohan Press 3")

  n=int(input("enter the number of user\n"))
  if n==1:
    print("for harry diet press 1\n","for harry exercise press 2")
    m = int(input())
    if m == 1:
        with open("harrydiet.txt") as f:
            a=f.read()
            print([getdate()])
            print(a)

    elif m == 2:
        with open("harryexercise.txt") as f:
            a=f.read()
            print([getdate()])
            print(a)
    else:
        print("invalid press,try again")
  elif n==2:
    print("for hamad diet press 1\n", "for hamad exercise press 2")
    m = int(input())
    if m == 1:
        with open("hamaddiet.txt") as f:
            a = f.read()
            print([getdate()])
            print(a)
    elif m == 2:
        with open("hamadexercise.txt") as f:
            a = f.read()
            print([getdate()])
            print(a)
    else:
        print("invalid press,try again")

  elif n==3:
    print("for rohan diet press 1\n", "for  rohan exercise press 2")
    m = int(input())
    if m == 1:
        with open("rohandiet.txt") as f:
            a = f.read()
            print([getdate()])
            print(a)
    elif m == 2:
        with open("rohanexercise.txt") as f:
            a = f.read()
            print([getdate()])
            print(a)
    else:
        print("invalid press,try again")

  else:
    print("invalid press!\n","press valid key")


 elif b==1:
     print("for harry Press 1,for hamad Press 2,for rohan Press 3")

     n = int(input("enter the number of user\n"))
     if n == 1:
         print("for harry diet press 1\n", "for harry exercise press 2")
         m = int(input())
         if m == 1:
             with open("harrydiet.txt","w") as f:
                 a = f.write(input("enter the new diet\n"))
                 print([getdate()])
                 print(a)
                 print("succesfully written")

         elif m == 2:
             with open("harryexercise.txt","w") as f:
                 a = f.write(input("enter the new exercise\n"))
                 print([getdate()])
                 print(a)
                 print("succesfully written")
         else:
             print("invalid press,try again")
     elif n == 2:
         print("for hamad diet press 1\n", "for hamad exercise press 2")
         m = int(input())
         if m == 1:
             with open("hamaddiet.txt","w") as f:
                 a = f.write(input("enter the new diet\n"))
                 print([getdate()])
                 print(a)
                 print("succesfully written")
         elif m == 2:
             with open("hamadexercise.txt","w") as f:
                 a = f.write(input("enter the new exercise\n"))
                 print([getdate()])
                 print(a)
                 print("succesfully written")
         else:
             print("invalid press,try again")

     elif n == 3:
         print("for rohan diet press 1\n", "for  rohan exercise press 2")
         m = int(input())
         if m == 1:
             with open("rohandiet.txt","w") as f:
                 a = f.write(input("enter the new diet\n"))
                 print([getdate()])
                 print(a)
                 print("succesfully written")
         elif m == 2:
             with open("rohanexercise.txt","w") as f:
                 a = f.write(input("enter the new exercise\n"))
                 print([getdate()])
                 print(a)
                 print("successfully written")
         else:
             print("invalid press,try again")

     else:
         print("invalid press!\n""try again")
 else:
     print("press valid key")