def solution(name):
    answer = 0
    n = len(name)
    
    move = n - 1
    
    # i 에서 방향 꺾으면 어떨지 계산 
    for i in range(n):
        # 1. 알파벳 변경 횟수
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        
        # 2. 커서 이동 횟수 
        # i 다음부터 연속된 A 구간 찾기
        next_idx = i + 1
        
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        
        # 오른쪽으로 갔다가 다시 왼쪽으로 돌아가는 경우
        move = min(move, 2 * i + n - next_idx)
        
        # 왼쪽으로 먼저 갔다가 오른쪽으로 돌아오는 경우
        move = min(move, i + 2 * (n - next_idx))
    
    return answer + move