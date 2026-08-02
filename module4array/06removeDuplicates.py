# Problem 5: Remove Duplicates
#Input [1,2,2,3,4,4,5]
#Output [1,2,3,4,5]
def duplicates(x):
    input = [1,2,2,3,4,4,5]
    seen = set()
    result = []
    for num in input:
      if num not in seen:
        seen.add(num)
        result.append(num)
    return result  
input = [1,2,2,3,4,4,5] 
print(duplicates(input))     