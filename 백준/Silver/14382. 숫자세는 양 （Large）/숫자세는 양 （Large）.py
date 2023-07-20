for t in range(1,int(input())+1):   
    x=int(input())
    if not x: print(f'Case #{t}: INSOMNIA')
    else:
        now=0
        cnt=0
        visited=[0]*10
        while cnt<10:
            now+=x
            temp=now
            while temp:
                if not visited[temp%10]:
                    cnt+=1
                    visited[temp%10]=1
                temp//=10
        print(f'Case #{t}: {now}')