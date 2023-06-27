def check_palindrome(input_string):
    # Remove spaces and punctuation from the string
    cleaned_string = "".join(char.lower() for char in input_string if char.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

def analyze_palindrome():
    print("Welcome to SocialConnect Language Analysis!")
    print("Please enter a string to check if it's a palindrome:")
    
    user_input = input()
    
    if check_palindrome(user_input):
        print(f'Thank you for providing the string.\nThe string "{user_input}" is a palindrome.')
    else:
        print(f'Thank you for providing the string.\nThe string "{user_input}" is not a palindrome.')

analyze_palindrome()
