n=int(input())
answer=0
A=tuple(map(int,input().split()))
B=tuple(map(int,input().split()))
K=tuple(map(lambda x: int(10*float(x)),input().split()))

for i in range(n):
    a = (A[i]*K[i])//10-B[i]
    b = A[i]-(B[i]*K[i])//10
    answer+=max(a,b)
    
print(answer)