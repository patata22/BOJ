def sol():
    A=tuple(map(int,input().split()))
    B=tuple(map(int,input().split()))
    if sum(A)>sum(B):return 'Algosia'
    elif sum(A)<sum(B):return 'Bajtek'
    else:
        for i in range(10,0,-1):
            a=A.count(i)
            b=B.count(i)
            if a>b: return 'Algosia'
            elif a<b:return 'Bajtek'
    return 'remis'

print(sol())

