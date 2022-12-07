f = list(map(int,input().split()))

while True:
    f[1]+=f[0]
    if f[1]>=5:
        print('yt')
        break
    f[0]+=f[1]
    if f[0]>=5:
        print('yj')
        break