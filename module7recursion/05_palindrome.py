#check palindrome using recursion
def pal(s):
    if len(s) <=1:
        return True
    if s[0] !=s[-1]:
        return False
    else:
        return pal(s[1:-1])
print(pal("lejkel")) 
print(pal("level"))    