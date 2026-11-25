
from collections import deque

# ==================================================
# ASSESSMENT 3.6: DFS METHODS IN TREE
# ASSESSMENT 3.3: NON-LINEAR DATA STRUCTURE
# Student: Richard T. Nacor Jr.
# ==================================================


# ==================================================
# PART 1: BINARY TREE
# ==================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# PREORDER: Root -> Left -> Right
def preorder(root, result):
    if root is not None:
        result.append(root.data)
        preorder(root.left, result)
        preorder(root.right, result)


# INORDER: Left -> Root -> Right
def inorder(root, result):
    if root is not None:
        inorder(root.left, result)
        result.append(root.data)
        inorder(root.right, result)


# POSTORDER: Left -> Right -> Root
def postorder(root, result):
    if root is not None:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.data)


# BINARY TREE BFS
def tree_bfs(root):
    if root is None:
        return []

    queue = deque([root])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current.data)

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    return result


# CREATE BINARY TREE
def create_binary_tree():

    root = Node("N")

    root.left = Node("A")
    root.right = Node("C")

    root.left.left = Node("O")
    root.left.right = Node("R")

    return root


# ==================================================
# PART 2: GRAPH (UNDIRECTED)
# ==================================================

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


# ==================================================
# PART 3: DISPLAY PROGRAM
# ==================================================

def main():

    root = create_binary_tree()

    print("=" * 55)
    print("       NON-LINEAR DATA STRUCTURE")
    print("       BINARY TREE AND GRAPH")
    print("       RICHARD T. NACOR JR.")
    print("=" * 55)

    # ----------------------------------------------
    # BINARY TREE
    # ----------------------------------------------

    print("\n[1] BINARY TREE STRUCTURE")

    print("""
             N
           /   \\
          A     C
         / \\
        O   R
    """)

    print("[2] BINARY TREE TRAVERSALS")

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

    # ----------------------------------------------
    # GRAPH
    # ----------------------------------------------

    print("\n[3] GRAPH STRUCTURE (UNDIRECTED)")

    print("Vertices: N, A, C, O, R")

    print("\nEdges:")
    print("(N, A)")
    print("(N, C)")
    print("(A, O)")
    print("(A, R)")
    print("(C, R)")

    print("\nGraph Adjacency List:")

    for vertex in graph:
        print(vertex, "->", ", ".join(graph[vertex]))

    # ----------------------------------------------
    # GRAPH TRAVERSALS
    # ----------------------------------------------

    print("\n[4] GRAPH TRAVERSALS")

    print("Starting Vertex: N")

    print("Graph DFS :", " -> ".join(graph_dfs("N")))

    print("Graph BFS :", " -> ".join(graph_bfs("N")))

    # ----------------------------------------------
    # END
    # ----------------------------------------------

    print("\n" + "=" * 55)
    print("             PROGRAM COMPLETED")
    print("=" * 55)


# RUN PROGRAM
if __name__ == "__main__":
    main()
