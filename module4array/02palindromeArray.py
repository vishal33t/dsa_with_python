#Problem 2: Check Palindrome Array
#Input [1,2,3,2,1]
#Output True
 
def palindrome(n):

   left = 0
   right =len(number)-1
   while left<right:
        if number[left]!=number[right]:
            return False
        left += 1
        right -= 1
        return True
number=  [1,2,3,2,1]
print(palindrome(number))        
