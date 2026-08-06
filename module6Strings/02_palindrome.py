# string palindrome using timeo(n) & space(n)

def spalindrome(input):
    blank = ""
    for i in input:
      blank = i + blank
      if blank == input:
        return True
    return -1  
input  = "LEVEL"
print(spalindrome(input))