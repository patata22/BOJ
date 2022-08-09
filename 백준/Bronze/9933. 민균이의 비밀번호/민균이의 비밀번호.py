words = set()
for _ in range(int(input())):
    words.add(input())
for word in words:
    if word[::-1] in words:
        print(len(word),word[len(word)//2])
        break
