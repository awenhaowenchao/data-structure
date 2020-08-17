#后序遍历
from src.chaptor_04.binary_tree import BinaryTree, Node


def after_search(node: Node):

    if node.left != None:
        after_search(node.left)

    if node.right != None:
        after_search(node.right)

    if node != None:
        print(node.value)


root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))

after_search(root)