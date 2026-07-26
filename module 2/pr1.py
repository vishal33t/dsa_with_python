#Medium
#Find the first non-repeating character.
#Check whether two strings are anagrams.
#Find duplicate numbers in a list.
#Count word frequencies in a sentence.
#Group words by their first letter.

def first_non_repeating(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char in s:
        if freq[char] == 1:
            return char
    return None

print(first_non_repeating("swiss"))
    