search_array =[int(x) for x in input("enter number with space:").split()]
feq = int(input("enter no to find frequency"))
count = 0
for i in search_array:
    if i == feq:
        count+= 1
print("Your array:", search_array)
print(count)
