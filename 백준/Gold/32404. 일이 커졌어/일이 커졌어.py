
n=int(input())
number=[i for i in range(1,n+1)]
odd = [number[i] for i in range(n//2,n)]
even=[number[i] for i in range(n//2)][::-1]
answer=[]
idx1=0
idx2=0
for i in range(n):
    if not i%2:
        answer.append(odd[idx1])
        idx1+=1
    else:
        answer.append(even[idx2])
        idx2+=1

print(*answer)