 #OOP stands for object oriented programming
 # A class is a blue print of an object
 # An object is a instance of a class
class Student :
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

        #member function
    def display(self):
        print(f"Student name is :{self.name},Age is: {self.age},score is : {self.score}")
#instance of the class (object)
myobj=Student( "Collins", 26,"A")
myobj.display()
myobj2=Student("James",17,'A')
myobj2.display()
myobj3=Student("Hannah",18,'B')
myobj3.display()
myobj4=Student("john", 16,'B')
myobj4.display()
myobj5=Student("Hanah",19,'B')
myobj5.display()

# create a file oop2 then create a class called cars with make ,model ,color ,yom,as the attributes
 # in a constructor method the a member function that prints (,...) Finally create 5 objects of the above