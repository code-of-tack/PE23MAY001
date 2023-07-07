class UserGraph:
    def __init__(self):
        self.graph = {}

    def add_user(self, user_id, connections):
        """
        Adds a user and their connections to the user graph.

        Args:
            user_id: The ID of the user.
            connections (list): The connections of the user.
        """
        self.graph[user_id] = connections

    def dfs_traversal(self, start_user):
        """
        Performs a depth-first search traversal on the user graph starting from the specified user.

        Args:
            start_user: The starting user ID for DFS traversal.

        Returns:
            list: The sequence of users visited during DFS traversal.
        """
        visited = []
        stack = [start_user]

        while stack:
            user = stack.pop()
            if user not in visited:
                visited.append(user)
                connections = self.graph.get(user, [])
                stack.extend(connections)

        return visited


def main():
    """
    Main function to run the SocialGraph - Explore Connections feature.
    """
    print("Welcome to SocialGraph - Explore Connections!")

    # Create a user graph
    user_graph = UserGraph()
    user_graph.add_user(12345, [56789])
    user_graph.add_user(56789, [98765])
    user_graph.add_user(98765, [43210])
    user_graph.add_user(43210, [])

    start_user = int(input("Please enter the starting user ID for DFS traversal: "))

    traversal_result = user_graph.dfs_traversal(start_user)

    print("\nThank you for providing the starting user ID.")
    print("DFS traversal result:")
    print(" -> ".join(str(user_id) for user_id in traversal_result))


# Run the program
if __name__ == '__main__':
    main()