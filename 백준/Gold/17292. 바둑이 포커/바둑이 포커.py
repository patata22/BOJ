def key(x):
    a,b,c,d=list(x)
    temp=0
    if a.isalpha():a=ord(a)-87
    else: a= int(a)
    if c.isalpha(): c=ord(c)-87
    else: c=int(c)

    if abs(a-c) in (1,14):
        temp+=10000000
    if a==c: temp+=1000000
    if b==d: temp+=100000
    temp+=1000*max(a,c)
    temp+=10*min(a,c)
    if (a>c and b=='b') or (c>a and d=='b'): temp+=1
    return -temp

card=input().split(',')
comb=[]
for i in range(6):
    for j in range(i+1,6):
        comb.append(card[i]+card[j])
comb.sort(key=lambda x: key(x))
for x in comb:
    print(x)
