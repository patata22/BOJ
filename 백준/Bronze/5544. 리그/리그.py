n=int(input())
score=[0]*(n+1)
for _ in range((n*(n-1))//2):
    a,b,c,d=map(int,input().split())
    if c==d:
        score[a]+=1
        score[b]+=1
    elif c>d: score[a]+=3
    else:score[b]+=3

result=sorted(score,reverse=True)
for i in range(1,n+1):
    print(result.index(score[i])+1)


