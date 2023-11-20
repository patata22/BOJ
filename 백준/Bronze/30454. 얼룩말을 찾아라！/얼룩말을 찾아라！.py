n,l=map(int,input().split())
maxline=0
answer=0

for _ in range(n):
    z=input()
    now='0'
    count=0
    for i in range(l):
        if now=='0' and z[i]=='1':
            count+=1
        now=z[i]
    if maxline<count:
        maxline=count
        answer=1
    elif maxline==count:
        answer+=1
print(maxline, answer)