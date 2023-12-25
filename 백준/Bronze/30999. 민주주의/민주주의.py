n,m=map(int,input().split())
answer=0
for _ in range(n):
    temp=input()
    if temp.count('O')*2>m:answer+=1
print(answer)
