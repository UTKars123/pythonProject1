#judging the number and limit the number of guess
n=50
guess=1
while(guess<=4):
 m=int(input("enter the number\n"))
 if m==n:
   print("you guess the right number and number of guess he took to finish is ",guess)
   break

 elif n<m:
   print("guess low value\n and number of guess remaining is ",4-guess)
 else:
    print("guess high value\n and number of guess remaining is ",4-guess)
 guess =guess + 1

if guess>4:
    print("Game Over")
    print("Right number is 50")