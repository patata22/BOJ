n,m=map(int,input().split())
MAX=m+64
answer=0
for _ in range(n):
    word=list(input())
    flag=True
    for x in word:
        if ord(x)>MAX: flag=False
    if len(word)!=len(set(word)):flag=False
    if flag:
        answer+=1
        
print(answer)
