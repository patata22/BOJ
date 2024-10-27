n=int(input())
m=int(input())
number=list(map(int,input().split()))

frame={}
vote=[0]*(m+1)
for i in range(m):
    now=number[i]
    if now in frame:
        frame[now][0]+=1
    else:
        if len(frame)==n:
            temp=[float('inf'),0]
            d=0
            for x in frame:
                target=frame[x]
                if target[0]<temp[0]:
                    temp=target
                    d=x
                elif target[0]==temp[0]:
                    if target[1]<temp[1]:
                        temp=target
                        d=x
            frame.pop(d)
        frame[number[i]]=[1,i]

print(*sorted([x for x in frame]))
