time=[0]*100001
n,q=map(int,input().split())
total=0
for i in range(1,n+1):
    song=int(input())
    for j in range(total,total+song):
        time[j]=i
    total+=song
for _ in range(q):
    print(time[int(input())])
