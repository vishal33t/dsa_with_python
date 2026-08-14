#Reverse every word in senetence
#Example : I Love Python
#OUTPUT  : I evoL nohtyP

text = "I Love Python"
result = ""
count_word = " "
for ch in text:
    if ch != ' ':
        count_word= ch +count_word
    else:
        result+= count_word +" "
        count_word =" "
result += count_word
print(result)            