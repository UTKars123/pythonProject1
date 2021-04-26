# f=open("happy.txt","rt")
#
# content=f.read(3)
# print(content)
#
# content=f.read(365)
# print(content)
#
# f.close()



# f=open("happy.txt","rt")
#
# content=f.read()
# print(content)
#
# f.close()

# f=open("happy.txt","rt")
#
# for line in f:
#     print(line)
#
# f.close()


# f=open("happy.txt","rt")
# print(f.readline())
# print(f.readline())
# f.close()

f=open("happy.txt","rt")
print(f.readlines())

f.close()



