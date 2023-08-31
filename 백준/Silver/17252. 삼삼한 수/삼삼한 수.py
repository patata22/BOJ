def sol(x):
    x=int(x)
    if not x: return 'NO'
    while x:
        if x%3==2: return 'NO'
        x//=3
    return 'YES'

print(sol(input()))
