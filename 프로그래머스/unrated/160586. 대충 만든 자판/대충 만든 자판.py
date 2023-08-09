def find_min_push(keymaps: list, target: str):
    res = 999
    for keymap in keymaps:
        try:
            res = min(res, keymap.index(target) + 1)
        except ValueError:
            continue
    return res


def solution(keymap, targets):
    answer = []

    for target in targets:
        push = 0
        for t in target:
            res = find_min_push(keymap, t)
            if res == 999:
                answer.append(-1)
                break
            else:
                push += res
        else:
            answer.append(push)
    return answer