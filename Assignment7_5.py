
def is_palindrome(text):
    
    text = text.replace(" ", "").lower()
    return text == text[::-1]


input_str = input("Enter a string: ")

if is_palindrome(input_str):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
