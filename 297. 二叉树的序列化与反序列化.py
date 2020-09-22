# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

     # 1.a 前序遍历 序列化 辅助函数
    def preorder_traversal_serialize(self, root: TreeNode, out_list: list):
        """
        :param out_list: List
        :param root: Node
        :return: [1, 2, #, #, 3, 5, #, #, #]
        """
        if not root:  # 空节点返回 #
            out_list.append(None)

        else:  # 非空节点
            out_list.append(root.val)
            self.preorder_traversal_serialize(root.left, out_list)
            self.preorder_traversal_serialize(root.right, out_list)

    # 1.a 序列化
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        temp = []
        self.preorder_traversal_serialize(root, temp)

        return str(temp)

    # 1.b 前序遍历 反序列化 辅助函数
    def preorder_traversal_deserialize(self, node_list: list):
        """
        :param node_list: list
        :return:
        """
        if not node_list:  # 列表空返回none
            return None

        else:  # 非空列表
            first_node_val = node_list[0]  # 取出第一个元素
            node_list.pop(0)  # 删除头一个元素

            if first_node_val == None:
                return None
            else:
                root = TreeNode(int(first_node_val))
                root.left = self.preorder_traversal_deserialize(node_list)
                root.right = self.preorder_traversal_deserialize(node_list)

                return root

    # 1.b 反序列化
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        temp_tree = eval(data)

        return self.preorder_traversal_deserialize(temp_tree)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
