def sol():
    F='TOO LATE'
    G='GOOD'
    y,m,d=map(int,input().split('-'))
    if y>2023: return F
    elif y<2023: return G
    if m>9: return F
    elif m<9: return G
    if d>16: return F
    return 'GOOD'

print(sol())
