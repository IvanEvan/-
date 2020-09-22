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
            while max_node.right:  # 先找到最右的最大值节点
                max_node = max_node.right

            self.helper(root, max_node)  # 递归 反向中序 从大到小排序

            return root
        else:
            return None

    def helper(self, root, max_root):
        global max_val
        if not root:
            return None

        else:  # 反向中序遍历
            self.helper(root.right, max_root)  

            if root == max_root:
                max_val = max_root.val  # 取出最大值节点对应的值
            else:
                root.val += max_val  # 累加节点值
                max_val = root.val

            self.helper(root.left, max_root)
