#Problem 4: Two Sum ⭐⭐⭐⭐⭐
#This is probably the most famous interview problem.
#Given arr = [2,7,11,15]    target = 9
#Output [0,1]
def twosum(n):
    target = 9
    for i in range (len(arr)):
      for j in range (i+1,len(arr)):
        if arr[i] + arr[j] == target:
           return [i,j]
arr = [2,7,11,15]   
print(twosum(arr))