# n=input("enter the numberto make astrologer star\n")
while 1:
 try:
    m = int(input("enter the numberto make astrologer star\n"))
    bool=int(input("press 1 for true ,press 0 for false\n"))
    if bool==1:
        i = 1
        while(i<=m):
            j=1
            while(j<=i):
                print("*",end="")
                j=j+1
            print(" ")
            i = i + 1
    elif bool==0:
        i = m
        while (0<i<= m):
             j = 1
             while (j <= i):
                 print("*", end="")
                 j = j + 1
             print("")
             i = i - 1
    else:
        print("invalid press!")
 except Exception as e:
     print(e)
