n=int(input())
series={}
point=0
for i,name in enumerate(input().split()):
    series[name]=i

answer=tuple(input().split())
for i in range(n):
    for j in range(i+1,n):
        if series[answer[i]]<series[answer[j]]:point+=1
m = (n*(n-1))//2
print(f'{point}/{m}')

