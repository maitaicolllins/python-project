'''
 """My name is colins maitai a former high school student / kaheti's school"""
print("a small boy in ")
video=" you tube "
video =" colins "
#
for x in range(10,20,5):
    print(" Am awesome")
#
name=10
while name  <20:
    print(name)
    name+=1
# continue
#number =int(input("input number here:"))
Numberstaken =[2,4,6,8,10]
print("Here are numbers available! ")
for n in range(1,20):
    if n in Numberstaken:
        continue
    print(n)


# functions
def name():
    print("Am a student in this class ")

def bitcoin_to_usd(btc):
    amount=btc*527
    print(amount)
name()
bitcoin_to_usd(200)

           #Girls I can date
def allow_dating_my_age(my_age):
    girl_age= my_age /2 + 7
    return girl_age

Collins_limit = allow_dating_my_age(20)
#Joe_limit =allow_dating_my_age(21)
print("Collins can date girls","collins_limit ","or older")
#print("Collins can date girls", "Joe_limit", "or older")
'''


           # set in making groceries list
groceries={'bread','maize','banana','apple','bread'}
print(groceries)
if 'bread' in groceries:
    print("I have bread")
else:
    print("you need milk")

              # health calculator
def health_calculator(age,apples_ate ,cigaretesmoked) :
    answer=(100-age)+(apples_ate * 3.5)-(cigaretesmoked*2)
    print(answer)
my_data=[27,4,0]
health_calculator(*my_data)