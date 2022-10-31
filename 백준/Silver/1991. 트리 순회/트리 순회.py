n = int(input())
tree = {}
for _ in range(n):
    t, l, r = input().split()
    tree[t] = (l, r)

def preorder(root): # root - 왼 - 오
    if root != '.':
        print(root, end="")
        preorder(tree[root][0])
        preorder(tree[root][1])
    return

def inorder(root): # 왼 - root - 오
    if root != '.':
        inorder(tree[root][0])
        print(root, end="")
        inorder(tree[root][1])
    return

def postorder(root): # 왼 - 오 - root
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end="")
    return

preorder('A')
print()
inorder('A')
print()
postorder('A')