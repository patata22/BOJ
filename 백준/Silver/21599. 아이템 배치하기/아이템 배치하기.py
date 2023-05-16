n=int(input())
number=sorted(list(map(int,input().split())), reverse=True)
cover=0
answer=0
for i in range(n):
    temp=min(i+number[i],n)
    answer+=max(temp-cover,0)
    cover=max(cover,temp)
print(answer)