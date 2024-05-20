n,m,k=map(int,input().split())
answer=n//(k-m)
if n%(k-m):answer+=1
print(answer)
