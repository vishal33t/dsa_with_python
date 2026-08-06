#Count frequency of characters in a string
def feqCount(character): 
    feq={}
    for ch in character:
       if ch in feq:
        feq[ch]+=1
       else:
        feq[ch] =1
    return feq
character = input("enter string  ")
print(feqCount(character))      