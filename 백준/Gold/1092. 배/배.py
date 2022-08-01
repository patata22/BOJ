import sys
input=sys.stdin.readline

n=int(input())
crane=sorted(list(map(int,input().split())),reverse=True)
m=int(input())
box=sorted(list(map(int,input().split())),reverse=True)
t=0
if crane[0]<box[0]:print(-1)
else:
    while box:
        for i in range(n):
            for j in range(len(box)):
                if crane[i]>=box[j]:
                    box.pop(j)
                    break
        t+=1
    print(t)