# 定义节点
class Node(object):
    def __init__(self, key=None, value=None):  # 节点有值 key value，以及指针 next 和 prev
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


# 定义双链表
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

        self.key_node = {}

        self.size = 0

    def add_node_last(self, x: Node()):  # 在链表尾部添加节点 x，时间 O(1)
        now_pre_node = self.tail.prev

        now_pre_node.next = x
        x.next = self.tail

        self.tail.prev = x
        x.prev = now_pre_node

        self.key_node[x.key] = x

        self.size += 1

    def remove_node(self, x: Node()):  # 删除链表中的 x 节点（x 一定存在，由于是双链表且给的是目标 Node 节点，时间 O(1)
        need_remove = self.key_node[x.key]

        now_prev = need_remove.prev  # x 节点当前前节点
        now_next = need_remove.next  # x 节点当前后节点

        now_prev.next = now_next
        now_next.prev = now_prev

        self.key_node.pop(x.key)

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


# 实现LFU
class LFUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity  # 缓存容量
        self.key_map_value = {}  # 存储 k--v
        self.key_map_frequence = {}  # 存储 k--f
        self.frequence_map_key_doublelist = {}  # 存储 f--链表
        self.min_frequency = 0  # 最小使用频率
        self.size = 0  # 当前缓存容量大小

    def operate_linklist(self, f):  # 根据f返回链表 新f返回空链表 旧f返回对应的链表
        if f not in self.frequence_map_key_doublelist:
            self.frequence_map_key_doublelist[f] = DoubleList()

        return self.frequence_map_key_doublelist[f]

    def change_frequence(self, key, new_one=False):  # 操作 f 相关的数据结构
        if new_one:  # 如果是新增的 k
            self.key_map_frequence[key] = 1

            double_linklist = self.operate_linklist(1)
            double_linklist.add_node_last(Node(key, self.key_map_value[key]))

        else:
            now_f = self.key_map_frequence[key]  # 取出当前 k 对应的 f
            after_f = now_f + 1  # f+1
            self.key_map_frequence[key] = after_f  # 同步更新到 k-f
            double_linklist = self.operate_linklist(after_f)
            double_linklist.add_node_last(Node(key, self.key_map_value[key]))

            self.frequence_map_key_doublelist[now_f].remove_node(Node(key, self.key_map_value[key]))  # 删除老f对应的node
            if len(self.frequence_map_key_doublelist[now_f]) == 0:
                self.frequence_map_key_doublelist.pop(now_f)

            # self.frequence_map_key_doublelist[after_f].add_node_last(Node(key, self.key_map_value[key]))  # 添加新f的node

    def get(self, key):
        if key in self.key_map_value:  # 如果 k 已存在
            self.change_frequence(key)
            return self.key_map_value[key]

        else:  # 如果 k 不存在 返回-1
            return -1

    def put(self, key, value):
        if key in self.key_map_value:  # 如果 k 已存在
            self.key_map_value[key] = value  # 更新 k-v
            self.change_frequence(key)

        else:  # k不存在
            if self.capacity != 0:
                if self.size < self.capacity:  # 当前容量小于总容量
                    self.key_map_value[key] = value  # 添加 k-v
                    self.change_frequence(key, new_one=True)
                    self.size += 1  # 当前容量+1

                else:  # 当前容量大于等于总容量
                    self.min_frequency = min(self.frequence_map_key_doublelist.keys())

                    minf_key_num = len(self.frequence_map_key_doublelist.get(self.min_frequency))
                    if minf_key_num == 1:  # 最小f对应只有一个值
                        old_key = list(self.frequence_map_key_doublelist[self.min_frequency].key_node.keys())[0]  # 取其对应的k
                        self.key_map_value.pop(old_key)  # 删除 k--v
                        self.key_map_frequence.pop(old_key)  # 删除 k--f
                        self.frequence_map_key_doublelist.pop(self.min_frequency)  # 删除 f--链表

                        self.key_map_value[key] = value  # 添加 k-v
                        self.change_frequence(key, new_one=True)
                        # self.size += 1  # 当前容量+1

                    if minf_key_num > 1:  # 最小的f对应多个node
                        need_rm_node = self.frequence_map_key_doublelist[self.min_frequency].remove_first()  # 删除 最久的链表node
                        rm_key = need_rm_node.key
                        self.key_map_value.pop(rm_key)  # 删除 k--v
                        self.key_map_frequence.pop(rm_key)  # 删除 k--f

                        self.key_map_value[key] = value  # 添加 k-v
                        self.change_frequence(key, new_one=True)
                        # self.size += 1  # 当前容量+1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
