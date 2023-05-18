def sol(start):
    global answer, total
    if start==n:
        if len(chosen)>=2 and chosen[-1]-chosen[0]>=x and l<=total<=r:
            answer+=1
        return
    sol(start+1)
    chosen.append(number[start])
    total+=number[start]
    sol(start+1)
    chosen.pop()
    total-=number[start]
    
n,l,r,x=map(int,input().split())
number=sorted(list(map(int,input().split())))
chosen=[]

total=0
answer=0

sol(0)
print(answer)