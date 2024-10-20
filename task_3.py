class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_of_bst(root):
    if root is None:
        return 0
    return root.value + sum_of_bst(root.left) + sum_of_bst(root.right)

root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(2)
root.right = TreeNode(20)

total_sum = sum_of_bst(root)
print(f"Сума всіх значень у дереві: {total_sum}")
