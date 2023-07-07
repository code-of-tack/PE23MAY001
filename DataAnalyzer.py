def sort_integers(numbers):
    """
    Sorts a list of integers in ascending order.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: The sorted list of integers.
    """
    return sorted(numbers)


def main():
    """
    Main function to run the DataAnalyzer Data Sorting feature.
    """
    print("Welcome to DataAnalyzer Data Sorting!")

    numbers = input("Please enter the list of integers you want to sort, separated by spaces: ").split()
    numbers = [int(num) for num in numbers]

    sorted_numbers = sort_integers(numbers)

    print("\nThank you for providing the list for sorting.")
    print("Here is the sorted list in ascending order:")
    print(" ".join(str(num) for num in sorted_numbers))


# Run the program
if __name__ == '__main__':
    main()