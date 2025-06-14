n, q = map(int, input().split())
lst = list(map(int, input().split()))

# 질의 입력받고 처리 
for i in range(q):
    # 질의 입력받기 
    qus = list(map(int, input().split()))
    
    # 첫 번째 질의: a번째 원소 출력 
    if qus[0] == 1:
        print(lst[qus[1]-1])

    # 두 번쨰 질의: index 출력, 없으면 0
    elif qus[0] == 2:
        if qus[1] in lst:
            print(lst.index(qus[1])+1)
        else:
            print("0")

    # 세 번째 질의: s~e번쨰 원소 출력, 공백 구분 
    elif qus[0] == 3:
        s = qus[1]-1
        e = qus[2]
        print(' '.join(map(str,lst[s:e])))
