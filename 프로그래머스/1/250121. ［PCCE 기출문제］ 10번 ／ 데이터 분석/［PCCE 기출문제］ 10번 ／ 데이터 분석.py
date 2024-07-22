def solution(data, ext, val_ext, sort_by):
    extStd = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    # data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값을 기준으로 오름차순으로 정렬
    data = list(filter(lambda x: x[extStd[ext]] < val_ext, data))
    data.sort(key=lambda x: x[extStd[sort_by]])

    return data