n,k,p=map(int,input().split())
number=tuple(map(int,input().split()))
answer=0
for i in range(0,n*k,k):
     count=0
     for j in range(k):
          count+=number[i+j]
     if count>=p: answer+=1
print(answer)       