n,k,p=map(int,input().split())
number=tuple(map(int,input().split()))
answer=n
for i in range(0,n*k,k):
     count=0
     for j in range(k):
          count+=number[i+j]
     if k-count>=p: answer-=1
print(answer)
     
     
             