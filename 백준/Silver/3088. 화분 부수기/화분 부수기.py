import sys
input=sys.stdin.readline

n=int(input())
answer=0
s=set()
for _ in range(n):
    a,b,c = map(int,input().split())
    if not (a in s or b in s or c in s):
        answer+=1
    s.add(a)
    s.add(b)
    s.add(c)

print(answer)
        
