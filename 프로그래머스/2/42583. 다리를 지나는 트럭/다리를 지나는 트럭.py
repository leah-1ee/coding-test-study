# 다리 길이만큼 큐 유지, 시뮬레이션 
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    bridge_weight = 0
    
    while truck_weights:
        time += 1
        bridge_weight -= bridge.popleft()
        
        if bridge_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            bridge.append(truck)
            bridge_weight += truck
            
        else:
            bridge.append(0)
    
    time += bridge_length
    
    return time