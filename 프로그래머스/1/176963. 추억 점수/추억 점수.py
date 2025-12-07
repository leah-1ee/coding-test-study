def solution(name, yearning, photos):
    answer = []
    
    # {이름: 점수} 저장할 딕셔너리 
    name_dict = {n:num for n, num in zip(name, yearning)}
    
    # 모든 사진의 점수 계산 
    for photo in photos:
        score = 0
        
        for person in photo:
            # 점수가 존재하는 사람이면 
            if person in name_dict:
                # 점수 추가 
                score += name_dict[person]
        
        # 사진 점수 기록 
        answer.append(score)
    
    return answer