def getDistance(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

sx,sy=map(int,input().split())
ex,ey=map(int,input().split())
point=[(sx,sy),(ex,ey)]
distance=[[float('inf')]*8 for i in range(8)]
for i in range(1,4):
    x1,y1,x2,y2=map(int,input().split())
    point.append((x1,y1))
    point.append((x2,y2))
    distance[i*2][i*2+1]=10
    distance[i*2+1][i*2]=10

for i in range(8):
    for j in range(8):
        x1,y1=point[i]
        x2,y2=point[j]
        temp=min(distance[i][j],getDistance(x1,y1,x2,y2))
        distance[i][j]=temp
        distance[j][i]=temp

for k in range(8):
    for i in range(8):
        for j in range(8):
            if distance[i][k]+distance[k][j]<distance[i][j]:
                distance[i][j]=distance[i][k]+distance[k][j]

print(distance[0][1])

