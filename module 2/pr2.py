#Check whether two strings are anagrams.
#Find duplicate numbers in a list.
#Count word frequencies in a sentence.
#Group words by their first letter.

def ang(s1,s2):
    s1 = s1.replace(" ","").lower()
    s1 = s1.replace(" ","").lower()
    if len(s1) != len(s2):
       return False   
    feq ={}
    for char in s1:
       feq[char] = feq.get(char, 0)+1
    for char in s2:
      if char not in feq:
       return False
      feq[char] -= 1
    if feq[char] < 0:
        return False

    return True


print(ang("hello","world"))
print(ang("listen","silent"))


   