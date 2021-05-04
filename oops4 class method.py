class employee:
    no_of_leaves=12
    def __init__(self,aname,asalary,arole):   #constructor automatic argument leta hai
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"name is {self.name},salary is {self.salary},role is {self.role}"

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves=new_leaves


happy=employee("happy",45,"instructor")   #abb isko init handle karega
rohan=employee("rohan",232,"student")

rohan.change_leaves(34)

print(happy.printdetails())
print(rohan.printdetails())     # self -rohan  .Code reusability ko badane ka kaam ho jaega
print(rohan.no_of_leaves)
print(employee.no_of_leaves)