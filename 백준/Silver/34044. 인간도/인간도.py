n=int(input())
answer=[1313131313131313131313 for i in range(n//11)]
n%=11
if n==0:print(''.join(map(str,answer)))
elif n==1: print(-1)
else:
    if n%2:
        n-=3
        answer.append(737319)
    for _ in range(n//2):
        answer.append(1331)
    print(''.join(map(str,answer)))