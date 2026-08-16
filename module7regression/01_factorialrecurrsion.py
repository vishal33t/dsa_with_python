def fact(n):
    if n ==0 or n==1:
     return 1
    else: 
     factorial = n* fact(n-1)
     return factorial
print(fact(4))    
print(fact(5))