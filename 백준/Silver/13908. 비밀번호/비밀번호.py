def check(x):
    for y in number:
        if y not in x: return 0
    return 1

n,m=map(int,input().split())
if not m:
    print(10**n)
else:
    number=input().split()
    answer=0
    for i in range(10**n):
        temp=str(i)
        answer+=check('0'*(n-len(temp))+temp)

    print(answer)
