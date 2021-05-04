import time
initial1=time.time()
k=0
while(k<45):
    print("this is me")
    k+=1
    time.sleep(1)
print("while loop run time",time.time()-initial1)
initial2=time.time()
i=0
for i in range(45):
    print("this is you")
    i+=1
print("for loop run time",time.time()-initial2)
# localtime=time.asctime(time.localtime(time.time()))
# print(localtime)