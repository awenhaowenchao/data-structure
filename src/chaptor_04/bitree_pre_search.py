#前序遍历
from src.chaptor_04.binary_tree import BinaryTree, Node


def pre_search(node: Node):

    if node != None:
        print(node.value)

    if node.left != None:
        pre_search(node.left)
    if node.right != None:
        pre_search(node.right)


root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))

pre_search(root)