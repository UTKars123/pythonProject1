# game development
i=1
a=0
b=0
while(i<=10):
    print("press1:gun,press2:water,press3:snake")
    n=int(input("enter the name of your choice\n"))


    import random
    lst=["gun","water","snake"]
    choice=random.choice(lst)
    print("random choice is ",choice)
    if n==1 and choice=="snake":
        a=a+1
        print("Your Team A point is ",a," chance remaining is ",10-i)
    elif n==1 and choice=="water":
        b=b+1
        print("Team B point is ",b,"lose"" Chance remaining is ",10-i)
    elif n==2 and choice=="gun":
        a = a + 1
        print("Your Team A point is ", a, " chance remaining is ", 10 - i)
    elif n==2 and choice=="snake":
        b=b+1
        print("Team B point is ",b,"lose"" Chance remaining is ",10-i)
    elif n==3 and choice=="water":
        a = a + 1
        print("Your Team A point is ", a, " chance remaining is ", 10 - i)
    elif n==3 and choice=="gun":
        b=b+1
        print("Team B point is ",b,"lose"" Chance remaining is ",10-i)
    i=i+1
    if i>10:
     if a>b:
        print("congratulation you are the winner")
     else:
        print("sorry you lose!")