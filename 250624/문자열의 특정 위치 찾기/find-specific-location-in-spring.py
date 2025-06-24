word, alp = input().split()

if alp in word:
    print(word.index(alp))
else:
    print("No")