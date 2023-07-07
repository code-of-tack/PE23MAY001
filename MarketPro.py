def find_kth_largest(nums, k):
    """
    Finds the kth largest element in an unsorted list.

    Args:
        nums (list): The unsorted list of elements.
        k (int): The value of k indicating the kth largest element to find.

    Returns:
        int: The kth largest element.
    """
    nums.sort(reverse=True)  # Sort the list in descending order
    return nums[k - 1]  # Return the kth largest element


def main():
    """
    Main function to run the MarketPro - Popular Products feature.
    """
    print("Welcome to MarketPro - Popular Products!")

    nums = input("Please enter the unsorted list of elements, separated by spaces: ").split()
    nums = [int(num) for num in nums]

    k = int(input("Please enter the value of k to find the kth largest element: "))

    kth_largest = find_kth_largest(nums, k)

    print("\nThank you for providing the value of k.")
    print("The kth largest element is:", kth_largest)


# Run the program
if __name__ == '__main__':
    main()