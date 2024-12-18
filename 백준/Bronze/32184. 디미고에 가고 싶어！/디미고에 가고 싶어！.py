a,b=map(int,input().split())
answer=0
if a%2==0:
    answer+=1
    a+=1
for i in range(a,b+1,2):
    answer+=1

print(answer)
