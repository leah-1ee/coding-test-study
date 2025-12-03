def solution(n):
    answer = 0
    
    # 3진수 저장
    base3 = ''
    
    # n -> 3진수 변환
    while n != 0:
        base3 = str(n%3) + base3
        n //= 3
    
    # 3진수 -> 10진수 변환
    base3 = base3[::]
    for i in range(len(base3)):
        answer += (3 ** i) * int(base3[i])
        
        
    return answer