n=int(input())
member=list(input().split())
vote={}
for m in member: vote[m]=0
for _ in range(n):
    temp = input().split()
    for m in temp: vote[m]+=1
member.sort(key= lambda x: (-vote[x], x))
for m in member:
    print(m, vote[m])
