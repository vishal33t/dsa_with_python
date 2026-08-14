#Find the most frequent character.
#Input: banana
#Output: a

def most_frequent_char(text):
    
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
            
    max_char = ""
    max_count = 0
    
    for char in char_counts:
        if char_counts[char] > max_count:
            max_count = char_counts[char]
            max_char = char
            
    return max_char

input_text = "banana"
output = most_frequent_char(input_text)
print(output)         