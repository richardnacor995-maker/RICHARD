
from collections import deque

# ==========================================
# BINARY TREE AND GRAPH
# Assessment 3.6
# Richard T. Nacor Jr.
# ==========================================


# ==========================================
# PART 1: BINARY TREE
# ==========================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root, result):
    if root:
        result.append(root.data)
        preorder(root.left, result)
        preorder(root.right, result)


def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.data)
        inorder(root.right, result)


def postorder(root, result):
    if root:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.data)


def tree_bfs(root):
    if root is None:
        return []

    queue = deque([root])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current.data)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return result


# CREATE BINARY TREE
def create_tree():

    root = Node("N")
    root.left = Node("A")
    root.right = Node("C")

    root.left.left = Node("O")
    root.left.right = Node("R")

    return root


# ==========================================
# PART 2: GRAPH (UNDIRECTED)
# ==========================================

graph = {
    "N": ["A", "C"],
    "A": ["N", "O", "R"],
    "C": ["N", "R"],
    "O": ["A"],
    "R": ["A", "C"]
}


# GRAPH DFS
def graph_dfs(start):

    visited = set()
    result = []

    def dfs(vertex):
        visited.add(vertex)
        result.append(vertex)

        for neighbor in sorted(graph[vertex]):
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return result


# GRAPH BFS
def graph_bfs(start):

    visited = {start}
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in sorted(graph[vertex]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


# ==========================================
# PART 3: MAIN PROGRAM
# ==========================================

def main():

    root = create_tree()

    print("=" * 50)
    print("       BINARY TREE AND GRAPH")
    print("       RICHARD T. NACOR JR.")
    print("=" * 50)

    # BINARY TREE
    print("\n[1] BINARY TREE STRUCTURE")

    print("        N")
    print("       / \\")
    print("      A   C")
    print("     / \\")
    print("    O   R")

    print("\n[2] BINARY TREE TRAVERSALS")

    result = []
    preorder(root, result)
    print("Preorder  :", " -> ".join(result))

    result = []
    inorder(root, result)
    print("Inorder   :", " -> ".join(result))

    result = []
    postorder(root, result)
    print("Postorder :", " -> ".join(result))

    print("Tree BFS  :", " -> ".join(tree_bfs(root)))

    # GRAPH
    print("\n[3] GRAPH STRUCTURE (UNDIRECTED)")

    print("Vertices: N, A, C, O, R")

    print("\nGraph Connections:")

    for vertex in graph:
        print(vertex, "->", ", ".join(graph[vertex]))

    # GRAPH TRAVERSALS
    print("\n[4] GRAPH TRAVERSALS")

    print("Starting Vertex: N")

    print("Graph DFS :", " -> ".join(graph_dfs("N")))
    print("Graph BFS :", " -> ".join(graph_bfs("N")))

    print("\n" + "=" * 50)
    print("          PROGRAM COMPLETED")
    print("=" * 50)


if __name__ == "__main__":
    main()
