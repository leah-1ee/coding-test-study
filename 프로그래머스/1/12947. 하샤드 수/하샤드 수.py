def solution(x):
    answer = False
    num_sum = sum(list(map(int, str(x))))
    if x % num_sum == 0:
        answer = True
    
    return answer