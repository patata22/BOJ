n,m=map(int,input().split())

answer=(n-1)*m+(m-1)*n
answer+=(n-1)*(m-2)*2
answer+=(n-1)*2
print(answer)
