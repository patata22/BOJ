def sol(x):
    x=int(x)
    if x==300:return 1
    elif x>=275:return 2
    elif x>=250: return 3
    return 4
input()
print(*map(lambda x: sol(x), input().split()))