# p.py
class P:
    def __init__(self, name, alias):
       self.name = name       # public
       self.__alias = alias   # private
 
    def who(self):
       print('name  : ', self.name)
       print('alias : ', self.__alias)    
 

# We create an instance of class P
#then trying to access its attributes whether it's public or private:
      
     
 #from P import P
 
x = P(name='Jessi', alias='Minnu')

print(x.name)
print(x._P__alias)