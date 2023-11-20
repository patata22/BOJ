n,t=map(int,input().split())
answer=[i for i in range(1,2*n+1)]
for i in range(2*n-1,1,-1):
    answer.append(i)
print(answer[t%len(answer)-1])