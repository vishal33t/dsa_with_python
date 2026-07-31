search_arr =[int(x) for x in input("enter number by follow space").split()]
secLargest =search_arr[0]
for num in search_arr:
    if secLargest<num:
        secLargest=num
print(secLargest)        
         