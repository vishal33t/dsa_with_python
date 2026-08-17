#sum of digits using recursion
def sum(n):
    if n==0:
        return 0
        
    else:
     print(n,end=" ")
     return (n%10) +(sum(n//10))
     
print(sum(12345))    