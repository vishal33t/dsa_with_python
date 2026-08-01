#Problem 1: Reverse an Array (Two Pointer)
   #Input [1,2,3,4,5]
# Output [5,4,3,2,1]
# Approach  left = 0    right = len(arr)-1
# Swap
# Move inward   
def rev(n):

   left = 0
   right =len(number)-1
   while left<right:
        number[left],number[right]=number[right],number[left]
        left += 1
        right -= 1
        return number
number=  [1,2,3,4,5]
print(rev(number))        
