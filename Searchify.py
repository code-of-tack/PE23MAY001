def binary_search(sorted_list, target):
    """
    Implements the binary search algorithm to find a target element in a sorted list.

    Args:
        sorted_list (list): A sorted list of elements.
        target: The element to search for.

    Returns:
        int: The index of the target element in the sorted list, or -1 if not found.
    """
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    """
    Main function to run the Searchify search feature.
    """
    print("Welcome to Searchify!")

    sorted_list = [1, 12, 20, 32, 42, 55, 67, 78, 90, 100]

    target = int(input("Please enter the element you want to search for: "))

    index = binary_search(sorted_list, target)

    if index != -1:
        print("\nThe element {} was found at index {}.".format(target, index))
    else:
        print("\nThe element {} was not found in the list.".format(target))


# Run the program
if __name__ == '__main__':
    main()