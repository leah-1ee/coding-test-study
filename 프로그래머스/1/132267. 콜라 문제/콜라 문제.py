def solution(a, b, n):
    answer = 0
    
    while n >= a:
        # 받을 수 있는 병 수
        answer += b * (n//a)
        # + 받을 수 있는 병 수 - 제출해야 하는 병 수
        n += (b-a) * (n//a)
    
    return answer