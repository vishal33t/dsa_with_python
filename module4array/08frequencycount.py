#Pattern 3: Frequency Counting
#Input [1,1,2,3,2,2]
input = [1,1,2,3,2,2]
seen = {}
for num in input:
    if num in seen:
        seen[num] += 1
    else:  
         seen[num] =1 
print(seen)         