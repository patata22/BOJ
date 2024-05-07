n=int(input())
finish=False
for i in range(1,87655):
    if finish: break
    cnt=[0]*10
    temp=i
    possible=True
    while temp:
        x=temp%10
        if cnt[x]:
            possible=False
            break
        cnt[x]=1
        temp//=10
    if possible:
        answer=True
        left=n-i
        if left==0: continue
        while left:
            if cnt[left%10]:
                answer=False
                break
            cnt[left%10]=1
            left//=10
    if answer:
        print(n-i,'+',i)
        finish=True
if not finish:print(-1)
