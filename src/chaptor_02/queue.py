from src.chaptor_02.arraylist import ArrayList
from src.chaptor_02.linkedlist import LinkedList


class Queue():
    """
    Queue队列，FIFO，分为如下两种：
        1，数组队列
        2，链式队列
    """

    def is_empty(self):
        pass

    def size(self):
        pass

    def push(self, item):
        pass

    def pop(self):
        pass

    def __str__(self):
        pass


class ArrayQueue():
    """
    ArrayQueue数组队列：
    """

    def __init__(self):
        self.data = ArrayList()

    def is_empty(self):
        return self.data.size()==0

    def size(self):
        return self.data.size()

    def push(self, item):
        self.data.add(item)

    def pop(self):
        if self.size()==0:
            raise ValueError('No element')
        self.data.remove(0)
        pass

    def __str__(self):
        return self.data.__str__()



class LinkedQueue():
    """
    LinkedQueue链式队列：
    """
    def __init__(self):
        self.data = LinkedList()
    def is_empty(self):
        return self.data.size()==0

    def size(self):
        return self.data.size()

    def push(self, item):
        self.data.append(item)

    def pop(self):
        self.data.remove(0)

    def __str__(self):
        return self.data.__str__()