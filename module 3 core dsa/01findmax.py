#Find the largest number.
number =[10,50,20,78,90,3,7]
maximum = number[0]
for num in number:
    if maximum<num:
        maximum = num
    

print(maximum)