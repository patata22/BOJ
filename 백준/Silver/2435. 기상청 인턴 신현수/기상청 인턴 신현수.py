n,k=map(int,input().split())

number=list(map(int,input().split()))

answer=sum(number[0:k])
temp=sum(number[0:k])
now=k
while now<len(number):
    temp+=number[now]
    temp-=number[now-k]
    now+=1
    answer=max(answer,temp)
print(answer)
