#5. Sum of 1 to N
#Example: n = 5
#1 + 2 + 3 + 4 + 5 = 15
#Recursive formula:   sum(n) = n + sum(n-1)
def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
print(sum(10))


#count digits e.g = 12345 = 5
def count(n):
    if n == 0:
        return 0
    else:
        return 1+count(n//10)
print(count(12345))    