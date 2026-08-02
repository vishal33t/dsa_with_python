#Problem 4: Two Sum ⭐⭐⭐⭐⭐
#This is probably the most famous interview problem.
#Given arr = [2,7,11,15]    target = 9
#Output [0,1]
def twosum(a,t):
   visited = {}
   for i in range (len(arr)):
    num = arr[i]
    complement = target-num

    if complement in visited:
     return ([visited[complement],i])
    else:
       visited[num] =i
arr = [2,7,11,15,3,5,9]
target = 24
print(twosum(arr,target))