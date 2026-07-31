# Reverse the given array

def reverse_array(arr):
    reversed_arr = []
    for item in arr:
        reversed_arr.insert(0, item)  # insert at front
    return reversed_arr

print(reverse_array([1, 2, 3, 4, 5])) 