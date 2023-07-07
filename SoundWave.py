# Function to perform merge sort
def merge_sort(arr):
    # Base case: return the list if its length is less than or equal to 1
    if len(arr) <= 1:
        return arr

    # Divide the list into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively call merge_sort on the left and right halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted left and right halves
    return merge(left, right)

# Function to merge two sorted lists
def merge(left, right):
    result = []  # List to store the merged result
    i = j = 0  # Pointers for the left and right lists

    # Compare the elements at indices i and j in the two lists
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append the remaining elements from the left and right lists
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Main program
playlist = [78, 56, 90, 120, 45, 80]
print("Welcome to SoundWave - Top Songs!")
print("Here is your unsorted playlist of song popularities:")
print(playlist)

sorted_playlist = merge_sort(playlist)  # Apply merge sort on the playlist

print("\nThank you for using SoundWave - Top Songs!")
print("Here is your sorted playlist in descending order of popularity:")
print(sorted_playlist)

