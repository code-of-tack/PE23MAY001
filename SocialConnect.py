#POV:You are part of a team developing a language processing and sentiment analysis tool for a popular social media platform called "SocialConnect." As part of this tool, you have been assigned the task of creating a feature that allows users to check if a given string is a palindrome or not. This feature will enable users to analyze and interpret user-generated content, such as comments or posts, and identify palindromic patterns that could impact sentiment analysis and user engagement.
def is_palindrome(n):
    return n == n[::-1]

def main():
    print("Welcome to SocialConnect Language Analysis!")
    input_str=input("Please enter a string to check if it's a palindrome: ")
    if is_palindrome(input_str):
        print("Thank you for providing the string.")
        print(f"The string '{input_str}' is a palindrome.")
    else:
        print("Thank you for providing the string.")
        print(f"The string '{input_str}' is not a palindrome.")

if __name__ == '__main__':
    main()