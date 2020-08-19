class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None
        

class LinkedList:
    """
    双向链式列表
    """
    def __init__(self):
        self._head:Node = None

    def add(self, item):
        """
        在头部添加节点
        :param item:
        :return:
        """
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def append(self, item):
        """
        在尾部添加节点
        :return:
        """
        if self.is_empty():
            self.add(item)
        else:
            node = Node(item)
            cur = self._head
            while None != cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, index, item):
        """
        在任意位置插入节点
        :param index:
        :param item:
        :return:
        """
        if index == 0:
            self.add(item)
        elif index+1 >= self.length:
            self.append(item)
        else:
            n = 1
            node = Node(item)
            cur = self._head
            while Node != cur:
                pre = cur
                cur = cur.next
                if n == index:
                    break
            pre.next = node
            node.prev = pre
            node.next = cur
            cur.prev = node

    def get(self, idx):
        if (self.size() < idx+1) or (idx < 0):
            raise BaseException("下标越界")

        count=0
        res:Node = self._head
        while True:
            if count==idx:
                return res.item
            else:
                res = self._head.next
                return res.item
            count+=1

    def size(self):
        """
        链表长度
        :return:
        """
        if self.is_empty():
            return 0
        n = 1
        cur = self._head
        while None != cur.next:
            cur = cur.next
            n += 1
        return n

    def delete(self, item):
        """删除节点元素"""
        if self.is_empty():
            raise ValueError('ERROR NULL')
        else:
            cur = self._head
            while None != cur:
                if cur.item == item:
                    if not cur.prev:  # 第一个节点
                        if None != cur.next:  # 不止一个节点
                            self._head = cur.next
                            cur.next.prev = None
                        else:  # 只有一个节点
                            self._head = None
                    else:  # 不是第一个节点
                        if cur.next == None:  # 最后一个节点
                            cur.prev.next = None
                        else:  # 中间节点
                            cur.prev.next = cur.next
                            cur.next.prev = cur.prev
                cur = cur.next

    def remove(self, idx):
        if (self.size() < idx+1) or (idx < 0):
            raise BaseException("下标越界")

        if self.size() == 1:
            self._head = None

        count = 0
        cur = self._head
        while None != cur:
            if count == idx:
                if not cur.prev:  # 第一个节点
                    if None != cur.next:  # 不止一个节点
                        self._head = cur.next
                        cur.next.prev = None
                    else:  # 只有一个节点
                        self._head = None
                else:  # 不是第一个节点
                    if cur.next == None:  # 最后一个节点
                        cur.prev.next = None
                    else:  # 中间节点
                        cur.prev.next = cur.next
                        cur.next.prev = cur.prev
            cur = cur.next
            count+=1



    def is_empty(self):
        """
        是否为空
        :return:
        """
        return None == self._head


    def __str__(self):
        """
        遍历链表
        :return:
        """
        tmp = []
        if self.is_empty():
            raise ValueError('ERROR NULL')
        cur = self._head
        tmp.append(cur.item)
        while None != cur.next:
            cur = cur.next
            tmp.append(cur.item)
        return str(tmp)