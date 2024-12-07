n=int(input())
left=list(enumerate(map(int,input().split())))
m=int(input())
right=list(enumerate(map(int,input().split())))

answer=[]
left.sort(key=lambda x: (-x[1],x[0]))
right.sort(key=lambda x: (-x[1],x[0]))

l=0
r=0
lidx=-1
ridx=-1
while True:
    if l>=n or r>=m: break
    if left[l][0]<lidx:
        l+=1
        continue
    if right[r][0]<ridx:
        r+=1
        continue
    if left[l][1]>right[r][1]:  l+=1
    elif left[l][1]<right[r][1]: r+=1
    else:
        answer.append(left[l][1])
        lidx=left[l][0]
        ridx=right[r][0]
        l+=1
        r+=1
        

print(len(answer))
print(*answer)
