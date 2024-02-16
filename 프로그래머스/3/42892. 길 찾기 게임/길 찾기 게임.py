import sys
sys.setrecursionlimit(10**6)

class Node():
    def __init__(self, i, pos):
        self.i = i
        self.pos = pos
        self.left = None
        self.right = None


def preorder(n: Node):
    path = [n.i]
    if n.left:
        path += preorder(n.left)
    if n.right:
        path += preorder(n.right)
    return path


def postorder(n: Node):
    path = []
    if n.left:
        path += postorder(n.left)
    if n.right:
        path += postorder(n.right)
    path.append(n.i)
    return path


def maketree(parent: Node, node):
    if parent.pos[0] > node[1]:
        if parent.left:
            maketree(parent.left, node)
        else:
            parent.left = Node(node[0], node[1:])
    else:
        if parent.right:
            maketree(parent.right, node)
        else:
            parent.right = Node(node[0], node[1:])


def solution(nodeinfo):
    nodeinfo = [(i + 1, x, y) for i, (x, y) in enumerate(nodeinfo)]
    nodeinfo.sort(key=lambda x: (-x[2], x[1])) #y값이 높으면 상위노드

    root = Node(nodeinfo[0][0], nodeinfo[0][1:]) # 루트노드로 초기화
    for i in nodeinfo[1:]:
        maketree(root, i)

    return [preorder(root), postorder(root)]