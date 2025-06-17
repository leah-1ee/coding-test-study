lst = [list(input().split()) for _ in range(5)]

for row in lst:
    print(' '.join([word.upper() for word in row]))