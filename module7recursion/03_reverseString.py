#7. Reverse a String using recursion
# Input: "python"
#Output: "nohtyp"
def rev(s):
    if len(s)<= 1:
        return s
    else:
        return s[-1]+rev(s[:-1])
print(rev("python"))    