#Problem 9: Majority Element (Easy Version)
#Input[2,2,1,2,3,2]
#Output 2
def maj(n):
    candidate = None
    count = 0
    for num in input:
     if count ==0:
        candidate= num

     if num==candidate:
        count+=1
     else:
        count-=1
    return candidate    
input = [2,2,1,2,3,2]
print(maj(input))            