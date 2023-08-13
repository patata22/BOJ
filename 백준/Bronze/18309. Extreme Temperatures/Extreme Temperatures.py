ma=-51
mi=51

while True:
    try:
        temp = input().split()
        t = list(map(int,temp[1:]))
        for x in t:
            ma=max(ma,x)
            mi=min(mi,x)
    except:break

print(mi,ma)

