# Creating of Class
class Employee:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname  = lastname
    
    def fullname(self):
        print(self.firstname)
        print(self.lastname)

# Call a Class inside a Object 

emp1 = Employee('Guido','Rossum')
print(emp1.fullname())

#print(emp1,type(emp1),id(emp1))


