f=open("happy.txt")
print(f.tell())
f.seek(9)  # t read text from 9th character
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
f.close()