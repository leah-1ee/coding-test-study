def solution(number):
    cnt = 0
    n = len(number)
    
    # 모든 조합 탐색
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                # 세 번호 합이 0이면 cnt +1
                if number[i] + number[j] + number[k] == 0:
                    cnt += 1
    
    return cnt