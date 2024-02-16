import sys
sys.setrecursionlimit(10**6)

def preorder(in_st, in_ed, post_st, post_ed):
    if in_st > in_ed or post_st > post_ed:
        return

    root = postorder[post_ed]
    left = loc[root] - in_st
    right = in_ed - loc[root]

    print(root, end=" ")
    # 재귀적으로 inorder의 루트 왼쪽은 왼쪽서브트리, 오른쪽은 오른쪽서브트리를 이룬다
    preorder(in_st, in_st+left-1, post_st, post_st+left-1)
    preorder(in_ed-right+1, in_ed, post_ed-right, post_ed-1)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

loc = [0]*(n+1)
for i in range(n):
    loc[inorder[i]] = i

preorder(0, n-1, 0, n-1)