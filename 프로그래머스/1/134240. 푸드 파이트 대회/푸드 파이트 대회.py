def solution(food):
    answer = ''
    n = len(food)
    
    # 1. 앞쪽 음식 배치 : 순서대로 음식 수 // 2 개 배치
    for i in range(1, n):
        answer += str(i) * (food[i]//2)
    
    # 2. 물 배치 : 0
    answer += '0'
    
    # 3. 뒤쪽 음식 배치 : 역순으로 음식 수 // 2 개 배치 
    for i in range(n-1, 0, -1):
        answer += str(i) * (food[i]//2)
    
    
    return answer