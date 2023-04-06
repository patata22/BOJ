import bisect

n=int(input())
number=[-float('inf')]+list(map(int,input().split()))

dp=[number[0]]
record=[0]*(n+1)
record[0]=(number[0],0)


for i in range(1,n+1):
    if number[i]>dp[-1]:
        record[i]=(number[i],len(dp))
        dp.append(number[i])
        
    else:
        idx = bisect.bisect_left(dp,number[i])
        dp[idx]=number[i]
        record[i]=(number[i],idx)

lis=[]
look= len(dp)-1
while look and record:
    num,idx = record.pop()
    if idx==look:
        lis.append(num)
        look-=1
        

print(len(dp)-1)
print(*lis[::-1])
