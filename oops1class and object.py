#classes- templates
#object-instance of the classes
#dry-don't repeat yourself

class student:
    pass
happy=student()
larry=student()
print(happy,larry)       #object instances
happy.name="Happy"       #instance variable
happy.std=12
happy.section=1
larry.std=8
larry.subject=["hindi","sanskrit","math","english"]
print(happy.name)
print(larry.subject)