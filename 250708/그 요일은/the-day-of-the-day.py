m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
# 각 달의 일 수 (인덱스 0은 사용 안 함)
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 월요일 기준 요일 인덱스 매핑
day_mapping = {
    "Mon": 0,
    "Tue": 1,
    "Wed": 2,
    "Thu": 3,
    "Fri": 4,
    "Sat": 5,
    "Sun": 6
}


# 1월 1일부터 해당 날짜까지 누적 일수 계산
start_day = sum(num_of_days[1:m1]) + d1
end_day = sum(num_of_days[1:m2]) + d2

# 특정 요일 수 세기 
day_count = (end_day - start_day + day_mapping[A]) // 7

print(day_count)