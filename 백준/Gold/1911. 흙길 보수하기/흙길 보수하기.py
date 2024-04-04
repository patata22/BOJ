import sys
input=sys.stdin.readline

n,l=map(int,input().split())
sink=[tuple(map(int,input().split())) for i in range(n)]
sink.sort()

now=0
answer=0
for s,e in sink:
    now=max(s,now)
    temp=(e-now)//l
    if (e-now)%l: temp+=1
    answer+=temp
    now+=temp*l
    
print(answer)
