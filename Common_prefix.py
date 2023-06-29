def longest_common_prefix(strings):
    if not strings:
        return ""

    prefix = strings[0]
    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Sample list of search results
search_results = [
    "apple pie recipe",
    "apple pie with cinnamon",
    "apple pie filling",
    "apple pie crust"
]

# Find the longest common prefix
common_prefix = longest_common_prefix(search_results)

# Display the results
print("Welcome to SearchMaster!")
print("Here are the search results related to your query:")
for i, result in enumerate(search_results, start=1):
    print(f"{i}. \"{result}\"")

print("\nThe longest common prefix among these search results is:", common_prefix)
