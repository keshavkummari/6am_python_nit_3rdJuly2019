class Human():
    # self : self represents object i.e. joel (a variable)
    # __init__ is constructer or inializer 
        def __init__(self,name,gender):   # __init__ is a method
            self.name = name     # Instance Variables
            self.gender = gender # Instance Variables
    
        def speak_name(self):
            print("My Name is %s" % self.name)
    
        def speak(self,text):
            print(text)

keshav = Human("KeshavKummari","Male")
#print(keshav.name)
#print(keshav.gender)

#print(keshav.speak_name())
print(keshav.speak("I Like Python Programming!"))