# while loop
num=1

while num <= 10:
    print(num)
    num+=1

    num3=5
    while num3<=50:
        print(num3)
        num3+=5

#for loop
Foods=['Ugali','Samaki','mchele','Chapati']
for f in Foods:
    print(f)
    print(len(f))
for num2 in range(1,11) :
    print(num2)
fruits=["Banana,""oranges,""Mangoes,""Avocado"]
for i in fruits:
    print(i)
jina="Emobilis"
for n in jina:
    print(n)
number=[4,-7,-4,9,2,1,6,7,6,5,12]
sum_even=0
for m in number:
    if m % 2==0:
        sum_even+=m
print(f"The sum of even is {sum_even}")

# calculate the sum of even numbers
# nested loop