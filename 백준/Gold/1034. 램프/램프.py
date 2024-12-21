n,m=map(int,input().split())

count={}
for _ in range(n):
    temp=input()
    if temp not in count:
        count[temp]=0
    count[temp]+=1
k=int(input())
answer=0

for x in count:
    need = x.count('0')
    if need>k: continue
    temp=k-need
    if temp%2==0: answer=max(answer,count[x])
print(answer)
