import sys
input=sys.stdin.readline

name={}
for t in range(int(input())):
    name[input().rstrip()]=t
fix=set([input().rstrip() for _ in range(int(input()))])
answer=sorted(name, key=lambda x:(x in fix, name[x]),reverse=True)
print(*answer,sep='\n')