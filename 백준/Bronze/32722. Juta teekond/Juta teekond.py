def sol():
    n='EI'
    if int(input()) not in (1,3): return n
    if int(input()) not in (6,8): return n
    if int(input()) not in (2,5): return n

    return 'JAH'

print(sol())