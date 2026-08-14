# check uppercase and lowercase character in sentennce

input = "Hello World"
lc = 0
uc =0
for ch in input:
    if 'A'<=ch <='Z':
        uc+= 1
    elif 'a'<=ch <='z':
        lc+=1
print(lc,uc)            