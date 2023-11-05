n=int(input())
l=input()
now=0
answer=0
for x in l:
    if x=='1':
        now=2
        answer+=1
    else:
        if now:
            now-=1
            answer+=1
print(answer)
        
