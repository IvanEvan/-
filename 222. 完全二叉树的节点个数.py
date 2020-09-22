# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:  # 空节点 返回个数为0
            return 0

        else:  # 非空  计算树的高度
            temp_left, temp_right = root, root  # 初始化复制左右根节点
            n_left, n_right = 1, 1  # 初始化树高

            while temp_left.left:  # 遍历最左树高度
                temp_left = temp_left.left
                n_left += 1

            while temp_right.right:  # 遍历最右树高度
                temp_right = temp_right.right
                n_right += 1

            if n_left == n_right:  # 如果最左、最右树高一样，则为 Perfect Binary Tree ，用公式 2**n-1 计算节点数
                return 2 ** n_left - 1

            else:  # 否则按普通方式计算
                return 1 + self.countNodes(root.left) + self.countNodes(root.right)
