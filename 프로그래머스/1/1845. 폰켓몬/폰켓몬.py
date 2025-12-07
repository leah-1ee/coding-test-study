def solution(nums):
    
    # 1. 가져갈 수 있는 폰켓몬의 최대 개수 (N/2)
    max_pick = len(nums) // 2
    
    # 2. 중복을 제거한 폰켓몬 종류의 개수
    unique_types = len(set(nums))
    
    # 3. 핵심 로직: 
    # 아무리 종류가 많아도 N/2마리보다 더 많이 가져갈 순 없고,
    # 아무리 많이 가져가고 싶어도 존재하는 종류 수(unique_types)를 넘을 순 없음.
    # 따라서 둘 중 더 작은 값이 정답이 됨
    return min(unique_types, max_pick)
