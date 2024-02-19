def getLeft(i):
    start=height[i]
    angle=-float('inf')
    count=0
    for j in range(i-1,-1,-1):
        angleNow = (height[j]-start)/(i-j)
        if angleNow>angle:
            angle=angleNow
            count+=1
    return count

def getRight(i):
    start=height[i]
    angle=-float('inf')
    count=0
    for j in range(i+1,n):
        angleNow = (height[j]-start)/(j-i)
        if angleNow>angle:
            angle=angleNow
            count+=1
    return count


n=int(input())
height=list(map(int,input().split()))
answer=0
for i in range(n):
    answer=max(answer, getLeft(i)+getRight(i))
print(answer)
