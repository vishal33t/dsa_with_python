#Find the minimum number.
number =[10,50,20,78,90,3,7]
minimum = number[0]
for num in number:
    if minimum > num:
        minimum = num

print(minimum)