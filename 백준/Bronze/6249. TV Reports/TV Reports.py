n,p,h=map(int,input().split())
for _ in range(n):
    x=int(input())
    if x>h:
        h=x
        print(f'BBTV: Dollar reached {h} Oshloobs, A record!')
    elif x<p:
        print(f'NTV: Dollar dropped by {p-x} Oshloobs')
    p=x