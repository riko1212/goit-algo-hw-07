class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_max_in_bst(root):
    if root is None:
        return None
    while root.right:
        root = root.right
    return root.value

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.right = TreeNode(30)

max_value = find_max_in_bst(root)
print(f"Найбільше значення у дереві: {max_value}")
