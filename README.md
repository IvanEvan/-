### 力扣刷题笔记
>  解决leetcode换设备登录后，已提交答案不再显示的问题

| 题目描述 | 难易程度 | 通过解法 | 解题思路 | 
| :---- | :----: | :----: | :---- |
| [98. 验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/) |  中等 | [solution](98.%20验证二叉搜索树.py) | **BST递归遍历，左小右大，辅助函数记录上下限** |
| [100. 相同的树](https://leetcode-cn.com/problems/same-tree/) |  简单 | [solution](100.%20相同的树.py) | **BST递归遍历，左小右大，辅助函数记录上下限，val相等** |
| [146. LRU缓存机制](https://leetcode-cn.com/problems/lru-cache/) |  中等 | [solution](146.%20LRU缓存机制.py) | **双向链接+hashmap（字典）** |
| [222. 完全二叉树的节点个数](https://leetcode-cn.com/problems/count-complete-tree-nodes/) |  中等 | [solution](222.%20完全二叉树的节点个数.py) | **普通二叉树遍历+满二叉树遍历** |
| [297. 二叉树的序列化与反序列化](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/) |  困难 | [solution](222.%20二叉树的序列化与反序列化.py) | **深度：前序、中序、后续遍历；广度：层级遍历** |
| [380. 常数时间插入、删除和获取随机元素](https://leetcode-cn.com/problems/insert-delete-getrandom-o1//) |  中等 | [solution](380.%20常数时间插入、删除和获取随机元素.py) | **O(1)哈希表，交换待删除元素到尾部，管理val list和val index字典** |
| [450. 删除二叉搜索树中的节点](https://leetcode-cn.com/problems/delete-node-in-a-bst/) |  中等 | [solution](450.%20删除二叉搜索树中的节点.py) | **分删除节点0个、1个、2个子节点三种情况** |
| [460. LFU缓存](https://leetcode-cn.com/problems/lfu-cache/) |  困难 | [solution](460.%20LFU缓存.py) | **比FRU多一个f（频率），待删除的最小f对应多个值时采用LRU** |
| [538. 把二叉搜索树转换为累加树](https://leetcode-cn.com/problems/convert-bst-to-greater-tree/) |  简单 | [solution](538.%20把二叉搜索树转换为累加树.py) | **反向中序遍历BST，节点从大到小排序** |
| [700. 二叉搜索树中的搜索](https://leetcode-cn.com/problems/search-in-a-binary-search-tree/) |  简单 | [solution](700.%20二叉搜索树中的搜索.py) | **左小右大，二分查** |
| [701. 二叉搜索树中的插入操作](https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/) |  中等 | [solution](701.%20二叉搜索树中的插入操作.py) | **左小右大，二分查，递归插左右** |
