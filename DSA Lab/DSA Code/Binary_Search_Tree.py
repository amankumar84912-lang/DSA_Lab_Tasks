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


def create_bst(characters):
    root = None

    for char in characters:
        root = insert(root, char)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


characters = input("Enter characters: ").split()

root = create_bst(characters)

print("Inorder traversal of BST:")
inorder(root)
