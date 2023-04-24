stack=list(input())
cnt=0
answer=0
while stack:
    now=stack.pop()
    if now==')':
        cnt+=1
    else:
        cnt-=1
        if cnt<0:
            answer+=1
            cnt+=1
answer+=cnt
print(answer)
    
