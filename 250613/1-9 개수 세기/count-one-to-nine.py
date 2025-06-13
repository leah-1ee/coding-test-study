n = input()
lst = list(map(int, input().split()))

count_arr = [0] * 9

# 카운트 배열에 개수 세기 
for num in lst:
    count_arr[num-1] += 1

for i in count_arr:
    print(i)