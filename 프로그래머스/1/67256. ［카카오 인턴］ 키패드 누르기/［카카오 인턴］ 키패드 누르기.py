# L = *  R = #
# 147 -> L  369 -> R
# 2580 -> 거리, hand

def solution(numbers, hand):
    answer = ''
    
    # 키패드 좌표 기록
    keypad = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }
    
    # 초기 손 위치 
    left_pos = keypad['*']
    right_pos = keypad['#']
    
    for num in numbers:
        # 147은 왼손 
        if num in (1, 4, 7):
            answer += 'L'
            left_pos = keypad[num]
        
        # 369는 오른손 
        elif num in (3, 6, 9):
            answer += 'R'
            right_pos = keypad[num]
        
        # 2580은 1. 거리 2. 주손
        else:
            # 1. 거리계산
            target_pos = keypad[num]
            
            l_dist = abs(left_pos[0] - target_pos[0]) + abs(left_pos[1] - target_pos[1])
            r_dist = abs(right_pos[0] - target_pos[0]) + abs(right_pos[1] - target_pos[1])
            # 거리가 더 적은 손으로 누름
            if l_dist < r_dist:
                answer += 'L'
                left_pos = keypad[num]
            elif l_dist > r_dist:
                answer += 'R'
                right_pos = keypad[num]
            
            # 2. 거리가 같을 경우 주손 사용 
            else:
                if hand == 'left':
                    answer += 'L'
                    left_pos = keypad[num]
                else:
                    answer += 'R'
                    right_pos = keypad[num]
    
    return answer