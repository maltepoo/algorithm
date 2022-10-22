def solution(str1, str2):
    str1,str2 = str1.upper(), str2.upper()
    str1_list, str2_list = [], []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            str1_list.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            str2_list.append(str2[i:i+2])
    inter = []
    uni = str1_list + str2_list
    for j in str1_list:
        if j in str2_list:
            inter.append(j)
            str2_list.remove(j)
    for j in inter: # 합집합 = 집합A + 집합B - A교집합B
        if j in uni:
            uni.remove(j)
    if len(uni) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(uni) * 65536)