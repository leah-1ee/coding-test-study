from collections import deque

def solution(maze):
    N = len(maze)
    M = len(maze[0])
    
    # 상하좌우 이동 벡터
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 시작/도착점 좌표 찾기
    for r in range(N):
        for c in range(M):
            if maze[r][c] == 1:
                startR = (r, c)
            elif maze[r][c] == 2:
                startB = (r, c)
            elif maze[r][c] == 3:
                endR = (r, c)
            elif maze[r][c] == 4:
                endB = (r, c)

    # 4차원 visited 배열: (rR, cR, rB, cB) 상태를 이미 방문했는지 기록
    
    # 큐 초기화: (턴 수, rR, cR, rB, cB, visitedR, visitedB)
    # visitedR/B는 각 수레가 방문한 좌표를 Set으로 기록
    # 두 수레가 동시에 이동하기 때문에 독립적인 배열이 아니라 둘의 위치 조합으로 관리해야 됨
    # 초기 상태: 0턴, 시작점, 시작점, {시작점}, {시작점}

    queue = deque([(0, *startR, *startB, {startR}, {startB})])

    # 중복 상태 체크를 위한 딕셔너리 (Set이 hashable하지 않으므로 사용 불가)
    # 단순 visitedR/B 체크는 턴마다 수행
    
    # 0턴 0초에 이미 목표에 도착했는지 확인
    if startR == endR and startB == endB:
        return 0

    # BFS 시작
    while queue:
        turn, rR, cR, rB, cB, visR, visB = queue.popleft()
        
        # 1. 종료 조건 확인 (모든 수레가 도착점에 멈춰야 함)
        if (rR, cR) == endR and (rB, cB) == endB:
            return turn
        
        # 2. 모든 수레의 이동 시도
        
        # 수레 R이 멈출지 (None) 이동할지 (0~3) 결정
        moveR_options = []
        if (rR, cR) == endR:
            moveR_options.append(None) # 멈춤
        else:
            moveR_options.extend(range(4)) # 상하좌우
            
        # 수레 B가 멈출지 (None) 이동할지 (0~3) 결정
        moveB_options = []
        if (rB, cB) == endB:
            moveB_options.append(None) # 멈춤
        else:
            moveB_options.extend(range(4)) # 상하좌우
        
        # 3. 모든 R 이동 경우의 수와 B 이동 경우의 수 조합 시도
        for moveR in moveR_options:
            
            # R이 멈춤
            if moveR is None:
                nR, nC = rR, cR
            # R이 이동
            else:
                nR, nC = rR + dr[moveR], cR + dc[moveR]
                
            # R이 이동 가능한지 1차 체크 (벽, 범위 밖, 방문했던 칸)
            if moveR is not None:
                if not (0 <= nR < N and 0 <= nC < M) or maze[nR][nC] == 5 or (nR, nC) in visR:
                    continue # R 이동 불가능

            for moveB in moveB_options:
                
                # B가 멈춤
                if moveB is None:
                    nBr, nBc = rB, cB
                # B가 이동
                else:
                    nBr, nBc = rB + dr[moveB], cB + dc[moveB]
                    
                # B가 이동 가능한지 1차 체크 (벽, 범위 밖, 방문했던 칸)
                if moveB is not None:
                    if not (0 <= nBr < N and 0 <= nBc < M) or maze[nBr][nBc] == 5 or (nBr, nBc) in visB:
                        continue # B 이동 불가능
                        
                # 4. 동시 이동 제약 및 자리 바꾸기 제약 체크
                
                # 4-1. 동시 같은 칸 이동 제약: nR, nC == nBr, nBc (두 수레가 같은 칸으로 이동 시도)
                if (nR, nC) == (nBr, nBc):
                    continue
                    
                # 4-2. 자리 바꾸기 제약: (R의 새 위치 == B의 이전 위치) AND (B의 새 위치 == R의 이전 위치)
                # (nBr, nBc) == (rR, cR) and (nR, nC) == (rB, cB)
                if (nBr, nBc) == (rR, cR) and (nR, nC) == (rB, cB):
                    continue
                    
                # 5. 다음 상태 큐에 삽입
                
                # 방문 경로 업데이트 (Set은 불변 객체가 아니므로 깊은 복사 필요)
                new_visR = visR.copy()
                new_visB = visB.copy()
                
                # 이동했을 때만 새 위치 추가
                if moveR is not None:
                    new_visR.add((nR, nC))
                if moveB is not None:
                    new_visB.add((nBr, nBc))
                    
                # 다음 상태를 큐에 추가
                queue.append((turn + 1, nR, nC, nBr, nBc, new_visR, new_visB))
                
    # 경로를 찾지 못한 경우
    return 0