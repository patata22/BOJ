n=int(input())
A=tuple(map(int,input().split()))
B=tuple(map(int,input().split()))
answer=0
for i in range(n):
    if A[i]>B[i]: answer+=3
    elif A[i]==B[i]:answer+=1
print(answer)
