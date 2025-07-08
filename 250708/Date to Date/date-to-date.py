m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 1월 1일부터 시작해 각 날짜까지 총 몇 일이 있는지
past, future = 0, 0

# 날짜 계산
for i in range(1, m1):
    past += num_of_days[i]

past += d1

for i in range(1, m2):
    future += num_of_days[i]

future += d2

# 날짜 차 출력 (시작일 포함)
print(future - past + 1)