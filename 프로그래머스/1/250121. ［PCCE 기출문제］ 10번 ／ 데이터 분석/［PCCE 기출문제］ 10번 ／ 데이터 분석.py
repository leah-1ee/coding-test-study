def solution(data, ext, val_ext, sort_by):
    answer = []
    

    # 필터링
    if ext == "code":
        answer = [d for d in data if d[0] < val_ext]
    elif ext == "date":
        answer = [d for d in data if d[1] < val_ext]
    elif ext == "maximum":
        answer = [d for d in data if d[2] < val_ext]
    elif ext == "remain":
        answer = [d for d in data if d[3] < val_ext]

    # 정렬
    if sort_by == "code":
        answer.sort(key=lambda x: x[0])
    elif sort_by == "date":
        answer.sort(key=lambda x: x[1])
    elif sort_by == "maximum":
        answer.sort(key=lambda x: x[2])
    elif sort_by == "remain":
        answer.sort(key=lambda x: x[3])

    return answer
