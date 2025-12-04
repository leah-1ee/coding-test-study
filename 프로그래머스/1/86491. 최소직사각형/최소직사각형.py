def solution(sizes):
    
    # 가로, 세로 사이즈 저장 
    w_wallet = 0
    h_wallet = 0
    
    # 모든 명함에 대해서 반복 
    for w, h in sizes:
        # 더 큰 길이가 가로, 더 짧은 길이가 세로가 되게 돌림 
        big = max(w, h)
        small = min(w, h)
        
        w_wallet = max(w_wallet, big)
        h_wallet = max(h_wallet, small)
        
    # 지갑 크기 리턴 
    return w_wallet * h_wallet 