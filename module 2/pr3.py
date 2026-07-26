#Find duplicate numbers in a list.
#Count word frequencies in a sentence.
#Group words by their first letter.
#   
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

print(find_duplicates([1, 2, 3, 2, 4, 1, 5]))  # Output: [1, 2]

def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

text = "This is a test this is only a test"
result = word_frequency(text)

for word, count in result.items():
    print(f"{word} -> {count}")
