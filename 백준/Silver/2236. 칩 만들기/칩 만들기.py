n,k=map(int,input().split())

answer=[0]*n

number=sorted(enumerate(map(int,input().split())),key=lambda x: x[1]**2)
count=0
for _ in range(k):
    if not number: break
    idx,x=number.pop()
    print(idx+1)
    answer[idx]=idx+1
    count+=1
for _ in range(k-count): print(0)

for i in range(n):
    print(answer[i])
