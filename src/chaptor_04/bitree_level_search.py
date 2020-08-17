#层次遍历
import collections

from src.chaptor_04.binary_tree import BinaryTree, Node


def level_search(node: Node):
    res, queue = [], collections.deque()
    if node != None:
        queue.append(node)
        while queue:
            n = queue.popleft()
            res.append(n.value)
            if n.left != None:
                queue.append(n.left)
            if n.right != None:
                queue.append(n.right)
    print(res)
root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))

level_search(root)