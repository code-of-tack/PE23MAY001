def find_longest_common_prefix(strings):
    if not strings:
        return ""

    min_length = min(len(s) for s in strings)
    longest_prefix = ""

    for i in range(min_length):
        char = strings[0][i]  # Get the character at index i from the first string
        if all(s[i] == char for s in strings):  # Check if all strings have the same character at index i
            longest_prefix += char  # Append the character to the longest prefix
        else:
            break  # Stop checking if the characters differ

    return longest_prefix


# Process user query
user_query = input("Enter your search query: ")

# Simulated search results for the user query
search_results = [
    "apple pie recipe",
    "apple pie with cinnamon",
    "apple pie filling",
    "apple pie crust"
]

# Display search results
print("Welcome to SearchMaster!")
print("Here are the search results related to your query:")
for i, result in enumerate(search_results, start=1):
    print(f"{i}. \"{result}\"")

# Find the longest common prefix
longest_prefix = find_longest_common_prefix(search_results)

# Display the longest common prefix
print(f"\nThe longest common prefix among these search results is: \"{longest_prefix}\"")
