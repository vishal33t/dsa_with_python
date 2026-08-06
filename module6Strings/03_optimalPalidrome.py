def pal(s):
   left = 0
   right = len(s)-1
   for ch in s:
      if left<right:
         if s[left]!=s[right]:
            return False

         left += 1
         right -=1
   return True   
 
s = input("enter the string") 
print(pal(s))       