n,m=map(int,input().split())
cake=sorted(list(map(int,input().split())), key =lambda x: (-(x%10), -x))
answer=0

while cake and m:
    now=cake.pop()
    if now==10: answer+=1
    elif now%10==0:
        temp = min(m, now//10-1)
        answer+=temp
        m-=temp
        if temp== now//10-1: answer+=1
    else:
        temp = min(m, now//10)
        
        answer+= temp
        m-=temp
print(answer)
       