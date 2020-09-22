# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:  # 为空则返回FALSE
            return TreeNode(val)

        # if val > root.val:  #  BST 中一般不会插入已存在元素

        if val > root.val:  # 目标值大于节点值 右子树查找
            root.right = self.insertIntoBST(root.right, val)

        if val < root.val:  # 目标值大于节点值 右子树查找
            root.left = self.insertIntoBST(root.left, val)
            
        return root
