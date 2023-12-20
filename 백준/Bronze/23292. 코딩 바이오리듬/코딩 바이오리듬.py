start=list(map(int,input()))
best=0
answer=0
days=[list(map(int,input())) for i in range(int(input()))]
days.sort()
for day in days:
    y,m,d=0,0,0
    for i in range(4):
        y+=(start[i]-day[i])**2
    for i in range(4,6):
        m+=(start[i]-day[i])**2
    for i in range(6,8):
        d+=(start[i]-day[i])**2
    total=y*m*d
    if total>best:
        answer=day
        best=total

print(''.join(map(str,answer)))