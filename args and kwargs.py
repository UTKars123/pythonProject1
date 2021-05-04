# def function_name(a,b,c,d):
#     print(a,b,c,d)
# function_name("happy","alok","rohan","watch")
def funargs(normal,*args,**kwargsbala):   #this * makes the argument as tuple
    print(normal)            #pt normal first then argument second
    for items in args:
        print(items)

    for key,value in kwargsbala.items():
        print(f"I am {key} and I eat {value}")

lst=("happy","alok","rohan","watch","honey")
kw={"happy":"pizza","rohan":"samosa","hamid":"paties","prachi":"buns"}
normal="I am the normal argument and the names are "
funargs(normal,*lst,**kw)

























































































