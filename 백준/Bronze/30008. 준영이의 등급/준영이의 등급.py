def grade(x):
    a=[96,89,77,60,40,23,11,4,0]
    for i in range(9):
        if a[i]<x: return 9-i
    return 1

n,k=map(int,input().split())
number=list(map(int,input().split()))
answer=[]
for x in number:
    answer.append(grade(100*x//n))
print(*answer)
    
