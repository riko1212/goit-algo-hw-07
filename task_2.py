class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_min_in_bst(root):
    if root is None:
        return None
    while root.left:
        root = root.left
    return root.value

root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(2)
root.right = TreeNode(20)

min_value = find_min_in_bst(root)
print(f"Найменше значення у дереві: {min_value}")
