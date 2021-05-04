class employee:
    no_of_leaves=12
    pass
happy=employee()
rohan=employee()
happy.nam="happy"
happy.salary=45
happy.role="instructor"
rohan.name="rohan"
rohan.salary=232
rohan.role="student"
print(rohan.role)
print(happy.no_of_leaves)
print(employee.no_of_leaves)
print(rohan.__dict__)
rohan.no_of_leaves=9       #it makes instant variable of object rohan
print(rohan.__dict__)
print(rohan.no_of_leaves)
print(employee.no_of_leaves)