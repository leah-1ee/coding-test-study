def solution(dartResult):
    score = [] # 점수를 담을 리스트
    
    # 1. 10을 한 글자인 'k'로 치환
    dartResult = dartResult.replace('10', 'k')
    
    for char in dartResult:
        # 2. 숫자인 경우 (점수 획득)
        if char.isdigit() or char == 'k':
            if char == 'k':
                score.append(10)
            else:
                score.append(int(char))
        
        # 3. 보너스 (S, D, T) - 가장 최근 점수(score[-1])를 가져와 계산
        elif char == 'S':
            # 1제곱은 값이 그대로니 생략 가능
            continue 
        elif char == 'D':
            score[-1] = score[-1] ** 2
        elif char == 'T':
            score[-1] = score[-1] ** 3
            
        # 4. 옵션 (*, #)
        elif char == '*':
            # 해당 점수 2배
            score[-1] *= 2
            # 바로 앞의 점수가 있다면 그것도 2배
            if len(score) > 1:
                score[-2] *= 2
        elif char == '#':
            # 해당 점수 마이너스
            score[-1] *= -1

    return sum(score)