#Part 2 – Binary Search ⭐⭐⭐⭐⭐
#This is one of the top 10 interview topics.
#Condition
#Binary Search only works on a sorted array.
#Correct [2,5,8,10,15,20]

def binary(arr, target):
    left = 0
    right = len(arr)-1
    while left<=right:
        middle = (left+right)//2
        if arr[middle]==target:
            return f"element found at index {middle}"

        elif target>middle:
            left = arr[middle]+1
        else:
            right = arr[middle]-1
    return -1

arr = [1,2,3,4,5,6,7,7,8,9]
target = 5
print(binary(arr,target))        
    