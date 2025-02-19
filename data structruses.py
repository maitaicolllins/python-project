# list data structers
# its ordered
# it has an index

fruits=["mangoes", "bananas" ,"oranges", "ovacado" , "grapes" ]
print(fruits)
fruits[1]="watermelon"
print(f"i love eating {fruits[1]}")
numbers=[1,2,3,4,5,6,-2,0,-1,-2]
numbers.sort()
numbers.append("pineapples")
numbers.pop(1)
numbers.reverse()
print(numbers[5])
#print(f"i want some {fruits[3]}")



# tuple datastructure
cars=("mercedes"",nissan,""toyota","subaru""ranger rover")
#cars[1]="suzuki"
nambari=( 3, 9, 2, 6, 9, 5, 7, 0,)
print(cars)
#cars.count()
print(f"japan produces {cars[1]}")
print(nambari)
print(sorted(nambari))

# set datastructures
# not ordered
# not index

country={"kenya","uganda","tanzania","burundi","dubai","mexico","rwanda","usa"}
print(country)
country.pop()
print(country)



# Dictionary datastructures
# key value pair

students={"name":"collins","Age":20,"Gender":"Male","phone number":112061289}
print(f"my name is {students['name']} and im {students['Age']} years old.")
print(f"my name is {students['name']} and im a {students['Gender']} this is my phone number {students["phone number"]}.")





