def solution(n):
    answer = 0
    i = 10 ** (len(str(n)) - 1)

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    while i >= 10:
        answer += (n // i)
        n %= i
        i /= 10
        
    answer += n
    
    return answer