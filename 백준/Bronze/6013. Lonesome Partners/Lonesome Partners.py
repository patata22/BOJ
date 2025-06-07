def calc(x1,x2,y1,y2):
    return (x1-x2)**2+(y1-y2)**2

maximum=0
answer=(0,0)
n=int(input())
point=[tuple(map(int,input().split())) for i in range(n)]
for i in range(n):
    x1,y1=point[i]
    for j in range(i+1,n):
        x2,y2=point[j]
        result=calc(x1,x2,y1,y2)
        if result>maximum:
            maximum=result
            answer=(i+1,j+1)
print(*answer)

