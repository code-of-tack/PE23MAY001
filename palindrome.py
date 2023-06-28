def is_palindrome(text):
    """
    Checks if a given string is a palindrome.

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove spaces and punctuation from the string and convert it to lowercase
    text = ''.join(char.lower() for char in text if char.isalnum())

    # Check if the string is equal to its reverse
    return text == text[::-1]


def main():
    """
    Main function to run the palindrome checker program.
    """
    print("Welcome to SocialConnect Language Analysis!")
    input_string = input("Please enter a string to check if it's a palindrome:\n")

    print("\nThank you for providing the string.")

    # Check if the input string is a palindrome
    if is_palindrome(input_string):
        print(f'The string "{input_string}" is a palindrome.')
    else:
        print(f'The string "{input_string}" is not a palindrome.')


# Run the program
if __name__ == '__main__':
    main()