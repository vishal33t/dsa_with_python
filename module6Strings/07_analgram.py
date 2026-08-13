#Problem 6 – Anagram ⭐⭐⭐⭐⭐
#Two strings are anagrams if they contain the same letters with the same frequencies.
#Examples listen  silent
#Output   True

def is_anagram(str1, str2):
     
    if len(str1) != len(str2):
        return False
    
    count1 = {}
    count2 = {}
    
    for char in str1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1
            
    for char in str2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1
            
    return count1 == count2

print(is_anagram("listen", "silent"))  # Output: True