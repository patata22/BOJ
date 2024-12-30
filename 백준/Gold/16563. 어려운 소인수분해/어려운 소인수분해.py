MAX=5000001

def change(x):
    result=[]
    while x!=1:
        result.append(prime[x])
        x//=prime[x]
    return result[::-1]

prime=[0]*MAX
for i in range(2,MAX):
    if not prime[i]:
        for j in range(i,MAX,i):
            prime[j]=i

input()
for x in input().split():
    print(*change(int(x)))
