# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.recursion_helper(root, float('inf'), float('-inf'))

    def recursion_helper(self, root: TreeNode(), now_max, now_min):  # 辅助函数 记录当前最大值和最小值
        if not root:  # 空节点合法
            return True

        if not root.left and root.val <= now_min:  # 左叶节点非空且左大于等于根 立判不合法
            return False

        if not root.right and root.val >= now_max:  # 右叶节点非空且右小于等于根 立判不合法
            return False

        return self.recursion_helper(root.left, root.val, now_min) and self.recursion_helper(root.right, now_max, root.val)  # 递归判断
