#first non repeating characters in a string
def first_uniq_char(s):
    
    frequency = {}
    for ch in s:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1
            
    for i in s:
        if frequency[i] == 1:
            return i  
            
    return -1  
print(first_uniq_char("leetcode"))  
print(first_uniq_char("loveleetcode")) 
print(first_uniq_char("aabb"))  