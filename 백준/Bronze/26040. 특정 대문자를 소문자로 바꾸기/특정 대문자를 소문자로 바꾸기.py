word=input()
for x in input().split():
    word=word.replace(x, x.lower())
print(word)
