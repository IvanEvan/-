# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:  # 都为空 则返回True
            return True
        
        elif bool(p) ^ bool(q):  # 如果一个空一个非空 返回False 用异或判断   
            return False
        
        else:  # 二者均非空  
            if p.val == q.val:  # 值相等  递归判断左右两节点
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
            else:  # 值不相等  返回False
                return False
