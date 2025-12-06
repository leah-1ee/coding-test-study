def solution(k, scores):
    # 최하위 점수 기록 배열, 명예의 전당 배열 
    answer = []
    honor = []
    
    for score in scores:
        # 명예의 전당 목록 채우기 
        if len(answer) < k:
            honor.append(score)
            
        else:
            # 더 높은 점수가 나오면 
            if score > min(honor):
                # 기존 점수 삭제, 새 점수 기록 
                honor.remove(min(honor))
                honor.append(score)
            
        # 최하위 점수 기록 
        answer.append(min(honor))
    return answer