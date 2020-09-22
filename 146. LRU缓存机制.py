# 1-2 实现哈希表 基于python字典
class HashTable(object):
    """
    实现一个定长的简单哈希表
    哈希函数使用线性探测
    k: Node 的映射
    """

    def __init__(self):
        self.dict_son = dict()

    def add_element(self, k, v):  # 添加元素
        self.dict_son[k] = v

    def remove_element(self, k):  # 删除元素
        if k in self.dict_son:
            self.dict_son.pop(k)

    def query_element(self, k, temp=None):  # 查询元素
        return self.dict_son.get(k, temp)

    def __len__(self):  # 哈希表非空值长度
        return len(self.dict_son)


# 2 实现双链表结构
# 2.1 定义链表的节点
class Node(object):
    def __init__(self, key=None, value=None):  # 节点有值 key value，以及指针 next 和 prev
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


# 2.2 定义双向链表
class DoubleList(object):
    def __init__(self):  # 初始化双向链表的数据
        """
            设置头尾，操作比较容易
            头－－（next）－－》尾
            尾－－（pre）－－》头
            :return:
        """
        head = Node()
        tail = Node()
        self.head = head
        self.tail = tail
        self.head.next = self.tail
        self.tail.prev = self.head

        self.key_node = HashTable()
        # self.head = Node()
        # self.tail = Node()
        #
        # self.head.next = self.tail
        # self.tail.prev = self.head

        self.size = 0

    def add_node_last(self, x: Node()):  # 在链表尾部添加节点 x，时间 O(1)
        now_pre_node = self.tail.prev

        now_pre_node.next = x
        x.next = self.tail

        self.tail.prev = x
        x.prev = now_pre_node

        self.key_node.add_element(x.key, x)

        self.size += 1

    def remove_node(self, x: Node()):  # 删除链表中的 x 节点（x 一定存在，由于是双链表且给的是目标 Node 节点，时间 O(1)
        need_remove = self.key_node.query_element(x.key)

        now_prev = need_remove.prev  # x 节点当前前节点
        now_next = need_remove.next  # x 节点当前后节点

        now_prev.next = now_next
        now_next.prev = now_prev

        self.key_node.remove_element(x.key)

        self.size -= 1

    def remove_first(self):  # 删除链表中第一个节点，并返回该节点，时间 O(1)
        maybe_need_rm = self.head.next
        if maybe_need_rm != self.tail:  # 确保除了 head 和 tail 以外中间有节点
            self.remove_node(maybe_need_rm)
            return maybe_need_rm
        else:
            return None

    def __len__(self):  # 链表长度
        return self.size


# 3 实现LRU
class LRUCache(object):
    def __init__(self, cap=2):
        self.dl = DoubleList()
        self.ht = HashTable()
        # 最大容量
        self.cap = cap

    def make_recently(self, key):  # 将某个已存在的 key 提升为最近使用的
        value = self.ht.query_element(key)
        # print(key, value)
        self.dl.remove_node(Node(key, value))  # 先从链表中删除这个节点
        self.dl.add_node_last(Node(key, value))  # 重新插到队尾

    def add_recently(self, key, value):  # 添加最近使用的新元素
        # print('ss', key, value)
        self.ht.add_element(key, value)  # 别忘了在 哈希表 中添加 key 的映射
        self.dl.add_node_last(Node(key, value))  # 链表尾部就是最近使用的元素

    def delete_key(self, key):  # 删除某一个 key
        value = self.ht.query_element(key)
        self.ht.remove_element(key)  # 从哈希表删
        self.dl.remove_node(Node(key, value))  # 从链表中删除这个节点

    def remove_least_recently(self):  # 删除最久未使用的
        remove_node = self.dl.remove_first()  # 链表头部的第一个元素就是最久未使用的
        self.ht.remove_element(remove_node.key)

    def get(self, key):
        if key in self.ht.dict_son:
            value = self.ht.query_element(key)  # 哈希表快速访问值
            self.make_recently(key)  # 链表操作更新为最新

            return value

        else:
            return -1

    def put(self, key, value):
        if key in self.ht.dict_son:  # 如果key已存在
            self.delete_key(key)
            self.add_recently(key, value)
        else:
            if len(self.dl) < self.cap:  # 判断是否大于容量
                self.add_recently(key, value)
            else:
                self.remove_least_recently()
                self.add_recently(key, value)
