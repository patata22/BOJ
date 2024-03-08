import sys
input=sys.stdin.readline

n,X=input().rstrip().split()
n=int(n)

answer=0
for _ in range(n):
    a,b=input().rstrip().split()
    a=a.split('_')
    for x in a:
        if x==X:
            answer+=int(b)
            break
print(answer)

