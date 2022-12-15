def choice(start, count):
    global answer
    if count==k:
        answer = max(answer,countWord())
        return
    for i in range(start, 123):
        if not choiced[i]:
            choiced[i]=1
            choice(i+1, count+1)
            choiced[i]=0

def check(word):
    for alpha in word:
        if not choiced[ord(alpha)]: return 0
    return 1

def countWord():
    temp = 0
    for word in words:
        temp += check(word)
    return temp

n,k=map(int,input().split())

answer=0
choiced = [0]*123
for a in 'antatica':
    choiced[ord(a)]=1
words=[input() for i in range(n)]

if k<5: print(0)
else:
    choice(97,5)
    print(answer)