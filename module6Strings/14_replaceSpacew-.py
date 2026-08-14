#replace  " " space with - 
def space(text):
   result = ""
   for ch in text:
     if ch ==' ':
       result+= '-'
     else:
        result += ch
   return result  
text = "you are my world"  
print(space(text))       
