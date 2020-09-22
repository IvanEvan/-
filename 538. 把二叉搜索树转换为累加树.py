# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            max_node = root
            while max_node.right:
                max_node = max_node.right

            self.helper(root, max_node)

            return root
        else:
            return None

    def helper(self, root, max_root):
        global max_val
        if not root:
            return None

        else:
            self.helper(root.right, max_root)

            if root == max_root:
                max_val = max_root.val
            else:
                root.val += max_val
                max_val = root.val

            self.helper(root.left, max_root)
