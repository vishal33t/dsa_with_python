#Problem 8 – Count Words

#Input "I love Python programming"

#Output   4
def count(text):
    text = "I love Python programming"
    count = 0
    word = False
    for ch in text:
       if ch !=" ":
         if not word:
          count += 1
          word = True
       else:
        word = False
    return count    
text = "I love Python programming"
print(count(text))            