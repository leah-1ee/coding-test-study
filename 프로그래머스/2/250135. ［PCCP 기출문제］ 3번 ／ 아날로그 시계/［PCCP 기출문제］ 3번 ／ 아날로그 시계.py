def count_alarms(seconds):
    """
    0초부터 주어진 시간(seconds) 직전까지 발생한 알람 횟수 계산 ([0, seconds) 구간).
    주기성 공식을 사용하여 겹침 횟수를 계산합니다.
    """
    
    # 초침과 분침이 겹치는 횟수 (1시간=3600초 동안 59회 발생)
    # 초당 59/3600회 발생
    minute_overlaps = (seconds * 59) // 3600
    
    # 초침과 시침이 겹치는 횟수 (12시간=43200초 동안 719회 발생)
    # 초당 719/43200회 발생
    hour_overlaps = (seconds * 719) // 43200
    
    # 0시/12시 정각에 시/분/초침이 모두 겹치는 횟수 (12시간마다 1회 발생)
    # 초침-분침 겹침과 초침-시침 겹침에서 2번 카운트되므로, 1번 빼서 중복을 제거해야 합니다.
    simultaneous = seconds // 43200

    # (초침-분침 겹침) + (초침-시침 겹침) - (동시 겹침 횟수)
    return minute_overlaps + hour_overlaps - simultaneous

def is_alarm(seconds):
    """
    주어진 시간(seconds)에 초침이 시침 또는 분침과 겹치는지 확인합니다.
    (각도 차이가 0이라는 의미, 나머지가 0인지 확인)
    """
    
    # 초침과 분침이 겹치는 조건 (주기 3600/59초의 배수인지 확인)
    # seconds * 59는 3600의 배수여야 함.
    if (seconds * 59) % 3600 == 0:
        return True
        
    # 초침과 시침이 겹치는 조건 (주기 43200/719초의 배수인지 확인)
    # seconds * 719는 43200의 배수여야 함.
    if (seconds * 719) % 43200 == 0:
        return True
        
    return False

def solution(h1, m1, s1, h2, m2, s2):
    
    # 시각을 0시 0분 0초부터의 총 초(second)로 변환
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2

    # 1. 시간 순환 처리 (23:59:59에서 00:00:00으로 넘어가는 경우는 없지만, 
    #   문제의 조건에 따라 h2시가 h1시보다 크므로 이 처리는 불필요할 수 있습니다. 
    #   하지만 겹침 계산의 정확성을 위해 12시간을 더하는 것은 안전한 방식일 수 있습니다.)
    if end <= start:
        end += 12 * 3600 # 12시간(43200초)을 더해 계산의 편의를 높입니다.

    # 2. [0, end) 구간 횟수에서 [0, start) 구간 횟수를 뺌
    #   -> (start, end) 구간의 횟수를 구함
    alarms = count_alarms(end) - count_alarms(start)

    # 3. T_start 시점 보정 (start 시각을 포함하기 위함)
    #   (start, end) 구간에 T_start 시점의 겹침이 누락되었으므로, 다시 더해줍니다.
    if is_alarm(start):
        alarms += 1

    return alarms