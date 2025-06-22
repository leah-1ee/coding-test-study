word1, word2 = input().split()

if len(word1) < len(word2):
    print(word2, end = " ")
    print(len(word2))

elif len(word2) < len(word1):
    print(word1, end = " ")
    print(len(word1))

else:
    print("same")