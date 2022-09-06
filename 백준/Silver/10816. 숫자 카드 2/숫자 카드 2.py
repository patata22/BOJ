input()
cnt={}
for x in list(map(int,input().split())):
    if x not in cnt:
        cnt[x]=1
    else:cnt[x]+=1
input()
for x in map(int,input().split()):
    if x not in cnt:print(0,end=' ')
    else:print(cnt[x],end=' ')
