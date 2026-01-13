def solution(board, moves):
    answer = 0
    # 인형을 쌓을 스택 
    stack = []
    
    # 인덱스 참조 위해 moves -1
    for i in range(len(moves)):
        moves[i] -= 1
    
    # 인형뽑기 기계 구현 
    for num in moves:
        for b in board:
            # 뽑기 기계 타겟 번호 
            target = b[num]
            
            if target != 0:
                # 같은 인형 두개가 쌓이면 스택에서 제거, answer +2
                if stack and target == stack[-1]:
                    stack.pop()
                    answer += 2
                
                # 같은 인형이 아니면 쌓기 
                else:
                    stack.append(target)

                # 뽑은 인형 제거 
                b[num] = 0
                break
                
    
    return answer