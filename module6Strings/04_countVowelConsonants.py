#Problem 3 – Count Vowels and Consonants ⭐⭐⭐⭐
#Input "education"
#Output Vowels: 5 Consonants: 4
def count_vowels(s):
    vowels = "aeiou"
    v = 0
    c = 0
    for ch in s.lower():
        if ch.isalpha():

            if ch in vowels:
                v += 1
            else:
                c += 1
    return v, c
print(count_vowels("education"))       