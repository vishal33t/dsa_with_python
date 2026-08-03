#Problem 6: Missing Number ⭐⭐⭐⭐
#Input [1,2,4,5]
#Output 3
#Formula Expected sum n*(n+1)//2   
input =[1,2,4,5]
n = 5   
sum =0  
expected = n*(n+1)//2 
for num in input:
    sum = sum+num
print(sum)
actual = sum
print(expected-actual)
       