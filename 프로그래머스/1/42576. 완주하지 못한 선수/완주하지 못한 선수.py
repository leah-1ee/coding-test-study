import collections
def solution(participant, completion):
    # 참가자들의 이름 개수 세기 (예: {'leo': 1, 'kiki': 2 ...})
    participant_count = collections.Counter(participant)
    
    # 완주자들의 이름 개수 세기
    completion_count = collections.Counter(completion)
    
    # 참가자 수에서 완주자 수 빼기
    answer = participant_count - completion_count
    
    # 남은 한 명의 키(이름)을 반환
    return list(answer)[0]
    
