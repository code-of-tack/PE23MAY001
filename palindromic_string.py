def check_palindrome(input_string):
    # Remove spaces and punctuation from the string
    cleaned_string = "".join(char.lower() for char in input_string if char.isalnum())

    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

def analyze_palindrome():
    # Welcome message for the Language Analysis feature
    print("Welcome to SocialConnect Language Analysis!")
    print("Please enter a string to check if it's a palindrome:")

    # Prompt the user to input a string
    user_input = input()

    # Check if the input string is a palindrome
    if check_palindrome(user_input):
        # Display a message if the string is a palindrome
        print(f'Thank you for providing the string.\nThe string "{user_input}" is a palindrome.')
    else:
        # Display a message if the string is not a palindrome
        print(f'Thank you for providing the string.\nThe string "{user_input}" is not a palindrome.')

# Call the analyze_palindrome function to start the program
analyze_palindrome()
