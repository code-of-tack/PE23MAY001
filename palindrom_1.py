def is_palindrome(string):
    # Remove spaces and punctuation from the string
    string = ''.join(c for c in string if c.isalnum())

    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Check if the string is equal to its reverse
    return string == string[::-1]

# User interaction
print("Welcome to SocialConnect Language Analysis!")
string = input("Please enter a string to check if it's a palindrome: ")

if is_palindrome(string):
    print("Thank you for providing the string.")
    print(f'The string "{string}" is a palindrome.')
else:
    print("Thank you for providing the string.")
    print(f'The string "{string}" is not a palindrome.')
