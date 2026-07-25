#Easy
#Remove duplicates from a list using a set.
#Find the union and intersection of two sets.
#Create a dictionary of five students and their marks.
#Print all keys and values.
#Count the frequency of each character in a string.


lst = [1,2,2,2,3,3,4,5,6,6,7,8,9,9]
lst1 = {1,2,3,4}
lst2 = {2,5,6,3}

student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eva": 88
}

text = "hello world"

# Initialize an empty dictionary
frequency = {}

# Loop through each character in the string
for char in text:
    # If character exists, increment its count; otherwise, set it to 1
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)



result = (lst1 | lst2) 
result2 = (lst1&lst2)
print(list(set(lst)))
print(result)
print(result2)
print(student_marks)
print(frequency)