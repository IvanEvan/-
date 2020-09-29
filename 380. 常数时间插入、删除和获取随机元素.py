import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_list = []  # 初始化一个list 用来存储val
        self.val_map_index = {}  # 初始化一个字典（哈希表） 来存储val到索引的映射

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val_list:  # 如果值已存在  返回False
            return False

        else:  # 插入尾部
            self.val_list.append(val)  # 先插入val列表尾部
            self.val_map_index[val] = self.val_list.index(val)  # 再插入 哈希表
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        交换val列表待交换的val和尾部val的位置  替换哈希表中二者的索引  并删除val
        """
        if val not in self.val_list:  # 如果不存在  返回False
            return False

        else:
            tar_val = val  # 待删除val
            tar_index = self.val_list.index(tar_val)  # 原先待删除val对应的index

            self.val_map_index[self.val_list[-1]] = tar_index  # 将哈希表尾部的val对应的index替换为原先待删除的index
            self.val_map_index.pop(tar_val)  # 删除哈希表中的val 及其对应的index

            self.val_list[tar_index], self.val_list[-1] = self.val_list[-1], self.val_list[
                tar_index]  # 待删除val 和列表末尾val 交换位置
            self.val_list.pop(-1)  # 删除末尾val
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.val_list[random.randint(0, len(self.val_list)-1)]
