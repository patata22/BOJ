import sys
input=sys.stdin.readline

n,A,B=map(int,input().split())
answer=0
number=[tuple(map(int,input().split())) for i in range(n)]
number.sort(key=lambda x: x[0]-x[1])
for i in range(A):
    answer+=number[i][0]
for i in range(A,n):
    answer+=number[i][1]
print(answer)
