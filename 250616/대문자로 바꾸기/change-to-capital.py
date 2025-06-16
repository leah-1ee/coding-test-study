lst = [list(input().split()) for _ in range(5)]

for i in range(5):
    for j in range(3):
        lst[i][j] = lst[i][j].upper()
        print(lst[i][j], end = ' ')

    print("\n", end='')