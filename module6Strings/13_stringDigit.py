#is digit contain any string or not

def is_all_digits(text):
    # Handle empty string edge case
    if text == "":
        return False
        
    for char in text:
        # If any character is outside '0' to '9', it's not all digits
        if not ('0' <= char <= '9'):
            return False
            
    return True

# Test the function
print(is_all_digits("12345"))  # Output: True
print(is_all_digits("123a45")) # Output: False
