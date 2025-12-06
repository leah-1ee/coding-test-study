import heapq

def solution(k, scores):
    # 최하위 점수 기록 배열, 명예의 전당 배열 
    answer = []
    honor = []
    
    for score in scores:
        # 명예의 전당 목록 채우기 
        heapq.heappush(honor, score)
        
        # 명예의 전당 명 수 초과 -> 가장 낮은 점수 삭제 
        if len(honor) > k:
            heapq.heappop(honor)
            
        # 최하위 점수 정답배열에 추가 
        answer.append(honor[0])
        
    return answer