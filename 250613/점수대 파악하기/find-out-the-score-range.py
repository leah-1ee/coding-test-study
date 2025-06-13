lst = list(map(int, input().split()))
count = [0]*10

# 점수대 세기 
for score in lst:
    if score == 0:
        break

    elif score >= 10:
        n = (score//10) -1
        count[n] += 1

for i, j in zip(range(100,0,-10), reversed(count)):
    print(f"{i} - {j}")