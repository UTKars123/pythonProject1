# import random
# rand=random.randint(1,6)
# #print(rand)
# ran=random.random()*100#it guess number in between 0 and 100
# #print(ran)
# lst=["aaj tak","strplus","sab tv","sony"]
# choice=random.choice(lst)
# print(choice


# print("\U0001f600")
# print("\U0001F923")
# print("\U0001F606")
# print("\U0001F640")
# import emoji
# print(emoji.demojize("😀"))
# print(emoji.emojize(":angry_face:"))


# import numpy
# arr=numpy.array([1,2,3,4,5])
# print(arr)

#
# # importing the library
# import pyperclip as pc
#
# text1 = "GeeksforGeeks"
#
# # copying text to clipboard
# pc.copy(text1)
#
# # pasting the text from clipboard
# text2 = pc.paste()
#
# print(text2)

import sys, pyperclip


# function to copy account passwords
# to clipboard
def manager(account):
    # dictionary in which keys are account
    # name and values are their passwords
    passwords = {"email": "Ayushi123",
                 "facebook": "shubham456",
                 "instagram": "Ayushi789",
                 "geeksforgeeks": "Ninja1"
                 }

    if account in passwords:

        # copies password to clipboard
        pyperclip.copy(passwords[account])

        print("Password :", passwords[account],
              ", for", account,
              "account",
              "has been copied to the clipboard")
    else:
        print("No such account record exits")


# Driver function
if __name__ == "__main__":
    # command line argument that is name of
    # account passed to program through cmd
    account = sys.argv[1]

    # calling manager function
    manager(account)

# This article has been contributed by
# Shubham Singh Chauhan
