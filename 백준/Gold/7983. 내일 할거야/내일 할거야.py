import sys
input=sys.stdin.readline

n=int(input())
work=[tuple(map(int,input().split())) for i in range(n)]
work.sort(key=lambda x: x[1])

a,b=work.pop()
start=b-a+1

while work:
    need,end=work.pop()
    if start>end:
        start=end-need+1
    else:
        start=start-need        
print(start-1)