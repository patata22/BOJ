for tt in range(int(input())):
    now=int(input())
    cnt=0
    while now!=6174:
        cnt+=1
        temp=list(str(now))
        while len(temp)<4: temp.append('0')
        sml=sorted(temp)
        big=sml[::-1]
        now=int(''.join(big))-int(''.join(sml))
    print(cnt)
