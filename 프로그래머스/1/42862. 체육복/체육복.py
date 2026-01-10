def solution(n, lost, reserve):
    # 본인이 도난당한 경우 제외 
    real_lost = set(lost) - set(reserve)
    real_reserve = set(reserve) - set(lost)
    
    for person in sorted(real_reserve):
        # 전 번호가 도난당함
        if person-1 in real_lost:
            real_lost.remove(person-1)

        # 뒤 번호가 도난당함 
        elif person+1 in real_lost:
            real_lost.remove(person+1)
        
    # 전체 인원 - 체육복을 빌리지 못한 사람 수 
    return n - len(real_lost)