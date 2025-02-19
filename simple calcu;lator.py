num=float(input("enter the first number:"))
num1=float(input("enter the second number:"))
operator=input("enter the operator(+,-,*,/)")


if operator =='+':
    result=num+num1
    print(f"the results of {num} {operator} {num1} is {result}")
elif operator == '-':
    result=num-num1
    print(f"the results of {num}{operator} {num1}is {result}")
elif operator =='*':
    result=num*num1
    print(f"the results of {num} {operator}{num1}is {result} ")
elif operator =='/':
    results=num/num1
    print(f"the results of {num} {operator} is {results}")
else:
    print(f"invalid input when ")
