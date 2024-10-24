n=int(input())
number=list(map(int,input().split()))
count=[0]*100001
for x in number:
    count[x]+=1
m = max(count)
print('NO') if m>n//2+n%2 else print('YES')
