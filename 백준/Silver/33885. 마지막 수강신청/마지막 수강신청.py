day={'MON':0, 'TUE':1, 'WED':2,'THU':3, 'FRI':4}

def parse(x):
    result=[]
    result.append(int(x[0]))
    for i in range(2,len(x),2):
        result.append(day[x[i]])
        result.append(int(x[i+1]))
    return result

def sol(depth):
    global flag
    if flag:return
    if depth==n:
        total=0
        for i in range(n):
            if used[i]:
                x=number[i]
                total+=x[0]
                for j in range(1,len(x),2):
                    time[x[j]][x[j+1]]+=1
        for i in range(5):
            for j in range(25):
                if time[i][j]>1: total=0
        if total>=m:flag=True
        for i in range(n):
            if used[i]:
                x=number[i]
                total+=x[0]
                for j in range(1,len(x),2):
                    time[x[j]][x[j+1]]-=1
        return
    sol(depth+1)
    used[depth]=1
    sol(depth+1)
    used[depth]=0

n,m=map(int,input().split())
number=[parse(input().split()) for i in range(n)]
time=[[0]*25 for i in range(5)]
used=[0]*n
flag=0
sol(0)
if flag:print('YES')
else:print('NO')