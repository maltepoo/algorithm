def solution(info, edges):
    answer = []

    tree = [[] for _ in range(len(info)+1)]

    for r, n in edges:
        tree[r].append(n)

    dfs(0, 1, 0, tree, [], answer, info)

    return max(answer)


def dfs(root, sheep, wolf, tree, visitable, answer, info):
    if sheep > wolf:
        answer.append(sheep)
    else:
        return

    visitable += tree[root]
    for node in visitable:
        new_visitable = list(visitable)
        new_visitable.remove(node)

        if info[node]:
            dfs(node, sheep, wolf + 1, tree, new_visitable, answer, info)
        else:
            dfs(node, sheep + 1, wolf, tree, new_visitable, answer, info)