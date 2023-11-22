import sys
input=sys.stdin.readline

n,q=map(int,input().split())
number=list(map(int,input().split()))
for _ in range(q):
    temp=list(map(lambda x: int(x)-1,input().split()))
    if temp[0]==0:
        a,b=temp[1],temp[2]
        answer=0
        for i in range(a,b+1):
            answer+=number[i]
        number[a],number[b]=number[b],number[a]
        print(answer)
    else:
        a,b,c,d=temp[1],temp[2],temp[3],temp[4]
        answer=0
        for i in range(a,b+1):answer+=number[i]
        for i in range(c,d+1):answer-=number[i]
        print(answer)