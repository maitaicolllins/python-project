

# create a file oop2 then create a class called cars with make ,model
# ,color ,yom,as the attributes
 # in a constructor method the
# a member function that prints (,...) Finally create 5 objects of the
# above

class cars :
    def __init__(self,make,model,color,yom):
        self.make =make
        self.model = model
        self.color= color
        self.yom= yom

    def display(self):
        print(f"Car make is :{self.make},model is {self.model},the color is {self.color} the year of manufacture is {self.yom}")
mycar=cars("Honda", "civic","dark blue",1902)
mycar.display()
mycar=cars("Mercedes","civic","dark blue",1900)
mycar.display()
mycar=cars("Tesla","civic","dark blue","1903")
mycar.display()
mycar=cars("Audi","civic","dark blue","1904")
mycar.display()





