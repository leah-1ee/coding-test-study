def solution(X, Y):
    answer = ''
    
    # 9부터 0까지 확인 - 정렬 불필요 
    for i in range(9, -1, -1):
        n = str(i)
        
        # 해당 숫자가 몇 번 있는지 세기 
        x_cnt = X.count(n)
        y_cnt = Y.count(n)
        
        # 더 적은 개수가 짝꿍 수 
        cnt = min(x_cnt, y_cnt)
        
        # 개수만큼 결과에 이어 붙이기 
        answer += (n * cnt)
    
    # 예외처리
    # 짝꿍 없는 경우 -1
    if answer == '':
        answer = '-1'
    # 짝꿍 전부 0인 경우 0
    elif answer[0] == '0':
        answer = '0'
  
    return answer