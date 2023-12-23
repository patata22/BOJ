for _ in range(int(input())):
    change={' ':' '}
    temp=list(input())
    nxt=list(input())
    for i in range(26):
        change[chr(i+65)]=nxt[i]
    print(''.join(map(lambda x: change[x],temp)))
    