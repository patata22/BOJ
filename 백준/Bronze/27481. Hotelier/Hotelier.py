room=[0]*10
input()
for x in input():
    if x=='L':
        for i in range(10):
            if not room[i]:
                room[i]=1
                break
    elif x=='R':
        for i in range(9,-1,-1):
            if not room[i]:
                room[i]=1
                break
    else:
        room[int(x)]=0
print(*room, sep='')
