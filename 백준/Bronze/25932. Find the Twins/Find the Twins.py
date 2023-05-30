for _ in range(int(input())):
    if _:print()
    x=tuple(map(int,input().split()))
    print(*x)
    if 17 in x and 18 in x:
        print('both')
    elif 17 in x: print('zack')
    elif 18 in x: print('mack')
    else: print('none')