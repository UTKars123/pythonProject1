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

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def print_good(string):
        print("this is a good\t"+ string)
happy=employee("happy",45,"instructor")
rohan=employee("rohan",232,"student")
karan=employee.from_dash("karan-348-teacher")
print(karan.print_good("happy"))