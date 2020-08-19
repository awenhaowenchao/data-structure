from src.chaptor_02.arraylist import ArrayList
from src.chaptor_02.linkedlist import LinkedList


class Stack():
    """
    Stack栈，LIFO，分为如下两种：
        1，数组栈
        2，链式栈
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


class ArrayStack():
    """
    ArrayStack数组栈：
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
        self.data.remove(self.data.size()-1)

    def __str__(self):
        return self.data.__str__()



class LinkedStack():
    """
    LinkedStack链式栈：
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
        self.data.remove(self.data.size()-1)

    def __str__(self):
        return self.data.__str__()