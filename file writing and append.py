# f=open("happy1.txt","w")  #w replace old content with  new content
# f.write("happy aacha baacha hai")
# f.close()

# f=open("happy1.txt","a")   #it appends old content along with new content
# f.write(" happy aacha baacha tha")
# f.close()

# f=open("happy1.txt","w")
# a=f.write("happy aacha baacha hai")
# print(a)
# f.close()
#handle both read and write both
f=open("happy.txt","r+")
print(f.read())
f.write("happy aacha baacha hai")
f.close()