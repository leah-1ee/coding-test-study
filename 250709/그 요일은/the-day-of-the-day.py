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


# 기준일과 종료일의 누적 일 수 계산
start_day = sum(num_of_days[1:m1]) + d1
end_day = sum(num_of_days[1:m2]) + d2

# 기준일이 월요일이므로 start_day 기준으로 day 0 (Mon)
# 따라서 i - start_day 로 계산

target_day = day_mapping[A]
day_count = 0

for i in range(start_day, end_day+1):
    if (i - start_day) % 7 == target_day:
        day_count += 1

print(day_count)