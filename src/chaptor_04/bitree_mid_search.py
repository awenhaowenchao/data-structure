#中序遍历
from src.chaptor_04.binary_tree import BinaryTree, Node


def mid_search(node: Node):

    if node.left != None:
        mid_search(node.left)

    if node != None:
        print(node.value)

    if node.right != None:
        mid_search(node.right)


root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))

mid_search(root)