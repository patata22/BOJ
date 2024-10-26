for tt in range(int(input())):
    l,r,s=map(int,input().split())
    left=s-l
    right=r-s
    if l==s or r==s:
        print(0)
        continue
    if right<=left:
        print(right*2)
    else: print(left*2+1)
