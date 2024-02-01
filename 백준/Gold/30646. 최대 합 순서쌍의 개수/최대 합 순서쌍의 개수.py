n=int(input())
number=list(map(int,input().split()))+[0]
left={}
right={}
for i in range(n):
    x=number[i]
    if x not in left: left[x]=i
    right[x]=i
for i in range(1,n):
    number[i]+=number[i-1]
answer=-float('inf')
count=0
for x in left:
    l = left[x]
    r = right[x]
    temp = number[r]-number[l-1]
    if temp>answer:
        answer=temp
        count=1
    elif temp==answer:
        count+=1
print(answer,count)