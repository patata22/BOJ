number=list(map(int,input().split()))
answer=0
for i in range(10):
    for j in range(i+1,10):
        answer^=number[i]|number[j]
        for k in range(j+1,10):
            answer^=number[i]|number[j]|number[k]
print(answer)
