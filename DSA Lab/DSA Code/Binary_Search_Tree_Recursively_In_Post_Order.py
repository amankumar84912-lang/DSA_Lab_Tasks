class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, char):
    if root is None:
        return Node(char)

    if char < root.data:
        root.left = insert(root.left, char)
    elif char > root.data:
        root.right = insert(root.right, char)

    return root


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


root = None

characters = input("Enter characters: ").split()

for char in characters:
    root = insert(root, char)

print("Postorder Traversal of BST:")
postorder(root)
