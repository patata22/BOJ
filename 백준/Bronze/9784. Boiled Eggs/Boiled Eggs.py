for t in range(1,int(input())+1):
    n,p,q = map(int,input().split())
    egg=list(map(int,input().split()))
    egg.sort()
    count=0
    weight=0
    for e in egg:
        if weight+e>q: break
        if count==p:break
        count+=1
        weight+=e
    print(f'Case {t}: {count}')
