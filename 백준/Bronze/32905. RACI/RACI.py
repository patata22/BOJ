answer='Yes'
n,m=map(int,input().split())
for _ in range(n):
    temp=input().split()
    if temp.count('A')!=1: answer='No'

print(answer)
