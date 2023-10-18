def check_pronounce(s):
    st = s
    for p in ["aya", "ye", "woo", "ma"]:
        if p*2 not in st:
            st = st.replace(p, "_")
    return st.replace("_", "")


def solution(babbling):
    answer = 0

    for bab in babbling:
        if not check_pronounce(bab):
            answer += 1
    return answer