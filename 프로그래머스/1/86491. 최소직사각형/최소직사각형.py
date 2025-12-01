def solution(sizes):
    
    # 지갑 가로, 세로 길이 
    wallet_w = 0
    wallet_h = 0
    
    # 모든 크기에 대해서 긴 쪽 -> 가로, 짧은 쪽 -> 세로 로 회전 
    for w, h in sizes:
        big = max(w, h)
        small = min(w, h)
        
        # 모든 크기에 대해 가장 긴 가로와 가장 긴 세로 찾기 
        wallet_w = max(wallet_w, big)
        wallet_h = max(wallet_h, small)
        
    # 지갑 크기 리턴 
    return wallet_w * wallet_h 