n=int(input())
limit=list(map(int,input().split()))
input()
for x in map(int,input().split()):
    limit[x-1]-=1
for x in limit:
    print('yes') if x<0 else print('no')
