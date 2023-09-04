now=1
input()
cmd=list(input())
answer=0
for x in cmd:
    if x=='L':
        if now!=1:now-=1
    else:
        if now!=3:now+=1
    if now==3: answer+=1
print(answer)
