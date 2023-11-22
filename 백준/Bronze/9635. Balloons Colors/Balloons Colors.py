for _ in range(int(input())):
    n,x,y=map(int,input().split())
    color=list(map(int,input().split()))
    if color[0]==x and color[-1]==y:print('BOTH')
    elif color[0]==x: print('EASY')
    elif color[-1]==y:print('HARD')
    else:print('OKAY')