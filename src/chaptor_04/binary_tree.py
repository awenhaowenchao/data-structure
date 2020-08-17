class Node():

    def __init__(self, value, left:"Node"=None,  right:"Node"=None):
        self.left = left
        self.value = value
        self.right = right

class BinaryTree():
    def __init__(self, root:"Node"):
        self.root = root



