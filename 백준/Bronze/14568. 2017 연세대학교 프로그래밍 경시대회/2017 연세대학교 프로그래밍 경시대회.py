n=int(input())
answer=0

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if i+j+k==n and j>=i+2 and not k%2: answer+=1

print(answer)
