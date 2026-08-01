#Problem 3: Move All Zeros to End ⭐⭐⭐⭐⭐
#Input [0,1,0,3,12]
#Output [1,3,12,0,0]
#Efficient Approach :Maintain a position for the next non-zero element.

arr =[0,1,0,3,12]
pos =0
for i in range(len(arr)):
    if arr[i]!= 0:
        arr[pos] ,arr[i] = arr[i],arr[pos]
        pos+= 1
print(arr)        
       