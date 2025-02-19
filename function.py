# Create a function called cars with the following parameters : model,make,year,color.
#then print a statement "the model of the cars is the make is manufactured in and the color .
#finally call the function five times with different arguments "
def cars(model,make,year,color):
    print(f"This car is {model} manufactured by {make} in the year {year} and it is {color} in color.")

cars(model='suv',make='Toyota',year='2020',color='black')
cars(model='convertable',make='Hyundai',year='2022',color='dark blue')
cars(model='sports car',make='Ferrari',year='2023',color='red')
cars(model='Cross over',make='Jeep',year='2024',color='white')
cars(model='Hatch back',make='Ford',year='2025',color='black')