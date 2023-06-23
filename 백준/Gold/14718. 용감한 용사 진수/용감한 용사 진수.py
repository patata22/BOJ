n,K=map(int,input().split())

soldier= [tuple(map(int,input().split())) for i in range(n)]
soldier.sort(key=lambda x: x[2])

answer=float('inf')
for i in range(n):
    x=soldier[i][0]
    for j in range(n):
        y=soldier[j][1]
        temp=0
        count=0
        for k in range(n):
            a,b,c=soldier[k]
            if a<=x and b<=y:
                count+=1
                temp=max(temp,c)
                if count==K: break
        if count>=K:answer=min(answer,x+y+temp)
print(answer)
                
        

