class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ==========================================
# 1. BINARY TREE TRAVERSALS
# ==========================================
def binary_tree_bfs(root):
    if not root:
        return

    queue = [root]
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current.data)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    print("Binary Tree BFS (Level-Order):", " -> ".join(result))


def binary_tree_dfs(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.data)
        binary_tree_dfs(root.left, result)
        binary_tree_dfs(root.right, result)
    return result


# ==========================================
# 2. GRAPH TRAVERSALS (Adjacency Matrix)
# Vertices: 0:N, 1:A, 2:C, 3:O, 4:R
# ==========================================
graph_vertices = ['N', 'A', 'C', 'O', 'R']

adj_matrix = [
    # N  A  C  O  R
    [0, 1, 1, 0, 0],  # N connects to A, C
    [1, 0, 0, 1, 1],  # A connects to N, O, R
    [1, 0, 0, 0, 1],  # C connects to N, R
    [0, 1, 0, 0, 0],  # O connects to A
    [0, 1, 1, 0, 0]  # R connects to A, C
]


def graph_bfs(start_index):
    visited = [False] * len(graph_vertices)
    queue = [start_index]
    visited[start_index] = True
    result = []

    while queue:
        current = queue.pop(0)
        result.append(graph_vertices[current])

        for i in range(len(graph_vertices)):
            if adj_matrix[current][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

    print(f"Graph BFS (starting at {graph_vertices[start_index]}):", " -> ".join(result))


def graph_dfs(start_index):
    visited = [False] * len(graph_vertices)
    result = []

    def dfs_helper(vertex):
        visited[vertex] = True
        result.append(graph_vertices[vertex])
        for i in range(len(graph_vertices)):
            if adj_matrix[vertex][i] == 1 and not visited[i]:
                dfs_helper(i)

    dfs_helper(start_index)
    print(f"Graph DFS (starting at {graph_vertices[start_index]}):", " -> ".join(result))


# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    print("========================================")
    print("     ASSESSMENT 3.3: NACOR TRAVERSALS   ")
    print("========================================\n")

    # Constructing Binary Tree for "NACOR"
    # Root: N
    # Level 1: A (left), C (right)
    # Level 2: O (left of A), R (right of A)
    root = TreeNode('N')
    root.left = TreeNode('A')
    root.right = TreeNode('C')
    root.left.left = TreeNode('O')
    root.left.right = TreeNode('R')

    print("--- BINARY TREE TRAVERSALS ---")
    binary_tree_bfs(root)
    dfs_result = binary_tree_dfs(root)
    print("Binary Tree DFS (Pre-Order):", " -> ".join(dfs_result))
    print()

    print("--- GRAPH TRAVERSALS ---")
    graph_bfs(0)  # Start at 'N' (index 0)
    graph_dfs(0)  # Start at 'N' (index 0)
    print("\n========================================")