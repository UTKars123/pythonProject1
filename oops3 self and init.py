class employee:
    no_of_leaves=12
    def __init__(self,aname,asalary,arole):   #constructor automatic argument leta hai
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"name is {self.name},salary is {self.salary},role is {self.role}"

happy=employee("happy",45,"instructor")   #abb isko init handle karega
rohan=employee("rohan",232,"student")

# happy.name="happy"
# happy.salary=45
# happy.role="instructor"
#
# rohan.name="rohan"
# rohan.salary=232
# rohan.role="student"
print(happy.printdetails())
print(rohan.printdetails())     # self -rohan  .Code reusability ko badane ka kaam ho jaega