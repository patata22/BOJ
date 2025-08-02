import sys,heapq
input=sys.stdin.readline

algo={}
for _ in range(int(input())):
    a,b=input().split()
    algo[a]=int(b)

member={}
for _ in range(int(input())):
    a,b=input().split()
    b=int(b)
    temp=[]
    for x in algo:
        temp.append((x,abs(algo[x]-b)))
    temp.sort(key=lambda x: (x[1],x[0]))
    member[a]=temp

now=''
for _ in range(int(input())):
    query=input().split()
    if query[-1][-1]=='!':
        print('hai!')
        now=query[0]
    else:
        print(member[now][1][0],member[now][0][0],sep=' yori mo ')