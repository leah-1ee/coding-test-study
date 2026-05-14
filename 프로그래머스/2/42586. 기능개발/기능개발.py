from collections import deque 

def solution(progresses, speeds):
    answer = []
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while(progresses):
        cnt = 0
        progresses = deque(p + s for p, s in zip(progresses, speeds))
        
        while progresses and progresses[0] >= 100:
            cnt += 1
            progresses.popleft()
            speeds.popleft()
        
        if cnt:
            answer.append(cnt)
    
    return answer