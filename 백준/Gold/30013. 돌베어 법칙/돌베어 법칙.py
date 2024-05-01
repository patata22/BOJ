def count(k):
    check=[0]*n
    result=0
    for i in range(n):
        if cry[i]=='#' and not check[i]:
            result+=1
            for j in range(i+k,n,k):
                if cry[j]=='#' and not check[j]:
                    check[j]=1
                elif cry[j]=='.':break
    return result
n=int(input())
cry=list(input())

answer=float('inf')
for i in range(1,n+1):
    answer=min(answer,count(i))


print(answer)
            
