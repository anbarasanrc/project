def is_palindrome(text):
    # Convert the text to lowercase and remove non-alphanumeric characters
    text = ''.join(e for e in text.lower() if e.isalnum())

    # Check if the text is equal to its reverse
    return text == text[::-1]

# Example usage
print(is_palindrome("racecar")) # prints True
print(is_palindrome("hello")) # prints False
