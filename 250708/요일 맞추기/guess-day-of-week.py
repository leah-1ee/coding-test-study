m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
# 각 달의 일 수 (인덱스 0 사용 안 함)
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 월요일 기준 요일 인덱스 매핑 
days = {
    0 : "Mon",
    1 : "Tue",
    2 : "Wed",
    3 : "Thu",
    4 : "Fri",
    5 : "Sat",
    6 : "Sun"
}

# 1월 1일부터 해당 날짜까지 누적 일 수 계산
past = sum(num_of_days[1:m1]) + d1
future = sum(num_of_days[1:m2]) + d2

# 요일: 차이 % 7
day = (future - past) % 7

print(days[day])