def seive():
    for i in range(2,119):
        if isPrime[i]:
            for j in range(i+i,119,i):
                isPrime[j]=0

isPrime=[1]*119
isPrime[0]=0
isPrime[1]=0
seive()
answer=['No']*238

for i in range(2,119):
    if isPrime[i]:
        for j in range(2,119):
            if isPrime[j]:
                answer[i+j]='Yes'
        
for _ in range(int(input())):
    print(answer[int(input())])

