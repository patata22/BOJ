import sys
input=sys.stdin.readline

stack=[]
count={}
answer=0
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a==1:
        if b not in count:
            count[b]=1
            stack.append(b)
        else: count[b]+=1
    else:
        if not stack: continue
        result=max(stack[-1]-b,0)
        if result not in count:
            count[result]=0
        while stack and stack[-1]>result:
            now=stack.pop()
            count[result]+=count[now]
            count[now]=0
        if not stack or stack[-1]!=result: stack.append(result)
            
for x in count:
    if count[x]: answer+=x*count[x]
print(answer)