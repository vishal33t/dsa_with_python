#bubble sort
def bubble(input):
    
    n = len(input)
    for i in range(n-1):
     for j in range(n-i-1):
        if input[j]>input[j+1]:
            input[j],input[j+1]= input[j+1],input[j]
    return input        
input = [5,3,8,4,2,7,7,6]
print(bubble(input))            