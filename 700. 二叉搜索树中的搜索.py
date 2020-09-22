# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        target = val
        if not root:  # 为空则返回FALSE
            return None

        if target > root.val:  # 目标值大于节点值 右子树查找
            return self.searchBST(root.right, target)

        elif target < root.val:  # 目标值大于节点值 右子树查找
            return self.searchBST(root.left, target)

        else:
            return root
