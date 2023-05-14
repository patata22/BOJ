from collections import Counter

def sol(count,char):
    global answer
    if count==n:
        answer+=1
        return
    for x in s:
        if s[x] and x!=char:
            s[x]-=1
            sol(count+1,x)
            s[x]+=1

s=Counter(input())
n=sum([s[x] for x in s])
answer=0
sol(0,'A')
print(answer)
