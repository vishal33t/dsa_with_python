#Linear search.
search =[10,50,20,78,90,3,7]
target = 90
for num in range(len(search)-1):
    if search[num]== target:
        print("Number found at index:",num)
