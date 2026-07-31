#count even number.
number =[10,50,20,78,90,3,7]
sum = 0
for num in number:
    if num%2 == 0:
        sum += 1
        print("even number in array:",num)

print("Total even numbers in an array are:",sum)
