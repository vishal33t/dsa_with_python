#Problem 7 – Remove Duplicate Characters
#Input programming

#Output   progamin
s = "programming"
seen = {}
noDup = ""
for ch in s:
    if ch in seen:
        seen[ch]+=1
    else:
        seen = 1    
