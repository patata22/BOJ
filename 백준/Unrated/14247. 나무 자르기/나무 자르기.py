n=int(input())
H=list(map(int,input().split()))
A=list(map(int,input().split()))

tree=[(H[i],A[i]) for i in range(n)]
tree.sort(key=lambda x: x[1])

answer=0
for i in range(n):
    answer+=tree[i][0]+i*tree[i][1]
print(answer)
