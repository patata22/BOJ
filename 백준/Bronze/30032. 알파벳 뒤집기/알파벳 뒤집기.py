change=[0,{'d':'q','b':'p','q':'d','p':'b'},{'d':'b','b':'d','q':'p','p':'q'}]
n,d=map(int,input().split())
for _ in range(n):
    print(''.join(map(lambda x: change[d][x], input())))