for tt in range(int(input())):
    n=int(input())
    cand=[]
    for _ in range(n):
        name=input()
        cnt=len(set(name))
        cand.append((name,cnt))

    cand.sort(key=lambda x: (-x[1],x[0]))

    print(f'Case #{tt+1}: {cand[0][0]}')
