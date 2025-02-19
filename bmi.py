# create a program that calculates your BMI
weight =int(input("Enter your weight in kilograms:"))
height=float(input("enter your height in metres: "))
print(f"Your BMI is  :{weight / (height * height)}")