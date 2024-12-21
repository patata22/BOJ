def sol(start):
    if start>n:
        if len(group)>=m:
            global answer
            temp=sorted(group)
            result=0
            for _ in range(m):
                result+=temp.pop()
            answer=max(answer,result)
            
        return
    for i in range(start,n+1):
        group.append(number[i]-number[start-1])
        sol(i+1)
        group.pop()

n,m=map(int,input().split())

number=[0]+list(map(int,input().split()))

for i in range(1,n+1):
    number[i]+=number[i-1]
answer=-float('inf')     
group=[]
sol(1)
print(answer)
