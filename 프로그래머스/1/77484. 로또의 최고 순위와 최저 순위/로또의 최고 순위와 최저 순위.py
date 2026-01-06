def solution(lottos, win_nums):
    # 최고, 최저 순위
    answer = []
    zeros = 0
    correct = 0
    
    # 등수 정의 - 맞힌 개수: 순위
    ranking = {
        6:1,
        5:2,
        4:3,
        3:4,
        2:5,
        1:6,
        0:6
    }
    
    # 맞힌 개수, 0 개수 세기 
    for num in lottos:
        if num in win_nums:
            correct += 1
        elif num == 0:
            zeros += 1
    
    # 최고 순위 - 알아볼 수 없는 단어가 모두 당첨 번호라고 가정 
    answer.append(ranking[correct+zeros])
    
    # 최저 순위 - 알아볼 수 없는 단어가 모두 당첨 번호가 아님 
    answer.append(ranking[correct])
    
    return answer