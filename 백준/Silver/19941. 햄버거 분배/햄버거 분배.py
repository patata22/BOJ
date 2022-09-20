n,k=map(int,input().split())

table=list(input())
eat=[0]*n
answer=0
for i in range(n):
    if table[i]=='P':
        for j in range(max(0,i-k),min(n,i+k+1)):
            if table[j]=='H' and not eat[j]:            
                eat[j]=1
                answer+=1
                break
print(answer)
