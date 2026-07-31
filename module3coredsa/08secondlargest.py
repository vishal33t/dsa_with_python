# find second largest number

search_arr =[int(x) for x in input("enter number by follow space").split()]
if len(search_arr) <2:
    raise ValueError("list must be greater than 2")
first = second = float('-inf')      
for num in search_arr:
    if num>first:
        second = first
        first=num
    elif num > second and num !=first:
        second = num   
    if second == float('-inf'):
        raise ValueError("No second largest element found (all elements may be equal)") 
print(second)