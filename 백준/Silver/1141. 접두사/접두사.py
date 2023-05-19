def choice(x):
    for w in answer:
        if x==w[:len(x)]: return False
    return True
        

word=[input() for i in range(int(input()))]
word.sort(key=lambda x: -len(x))

answer=[]
for w in word:
    if choice(w):answer.append(w)
print(len(answer))