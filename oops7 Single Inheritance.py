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

class programmer(employee):
    no_of_holidays = 34
    def __init__(self,aname,asalary,arole,alanguage):
        self.name = aname        #ye kaam chalau hai iski jagah par Super(class kea constructor ko call karata hai) ka use karte hai
        self.salary = asalary
        self.role = arole
        self.language=alanguage

    def printprog(self):
        return f"The programmer name is {self.name},salary is {self.salary},role is {self.role} and the language are {self.language}"

happy=employee("happy",45,"instructor")
rohan=employee("rohan",232,"student")

shubham=programmer("shubham","4354","teacher",["python"])
karan=programmer("karan","45","programmer",["python","cpp"])
print(karan.printprog())
print(karan.printdetails())
print(karan.no_of_holidays)