n=int(input())
number=tuple(map(int,input().split()))
answer='yes'
for i in range(n):
    for j in range(n):
        if i==j: continue
        for k in range(n):
            if j==k or i==k: continue
            x=(number[i]-number[j])/number[k]
            if x!=int(x):  answer='no'
print(answer)
