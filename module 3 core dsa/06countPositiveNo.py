# Count Positive number in an array 
number = [-2, 5, -7, 8, 10, -1]
sum = 0
for num in number:
    if num > 0:
        sum += 1
        print("positive number in array:",num)

print("Total positive numbers in an array are:",sum)