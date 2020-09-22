# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int):
        def get_left_max(sub_root: TreeNode):
            while 1:  # 最大值都在最右下角的节点
                if sub_root.right:
                    sub_root = sub_root.right
                else:
                    return sub_root

        if not root:
            return None

        if key < root.val:  # 1. 目标值小于当前节点值 去左子树遍历
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:  # 2. 目标值大于当前节点值 去右子树遍历
            root.right = self.deleteNode(root.right, key)

        else:  # 3. 是要删除的节点 root.val == key
            if not root.left and not root.right:  # 3.1 左右节点皆为空即为尾节点
                return None

            if bool(root.left) ^ bool(root.right):  # 3.2 如果只有左或者只有右节点  ^:异或运算
                if not root.left:  # 如果没有左  将当前root指定为右节点
                    return root.right
                else:  # 如果没有右  将当前root指定为左节点
                    return root.left

            if root.left and root.right:  # 3.3 左右节点均有值 取左节点的最大值或右节点的最小值替换root的值 并删除对应的半边节点的该值
                max_val_root = get_left_max(root.left)  # 找出root的左节点中最大值
                root.val = max_val_root.val  # 将此值替换为root的值
                root.left = self.deleteNode(root.left, max_val_root.val)  # 删除root的左节点中的最大值节点 返回新的root左节点

        return root
