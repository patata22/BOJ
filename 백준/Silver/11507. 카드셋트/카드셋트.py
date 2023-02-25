p,k,h,t=13,13,13,13
P,K,H,T=set(),set(),set(),set()
s=input()
answer=0
for i in range(0,len(s),3):
    temp=s[i:i+3]
    a=temp[0]
    n=int(temp[1:])
    if a=='P':
        if n in P:
            answer="GRESKA"
            break
        else:
            p-=1
            P.add(n)
    elif a=='K':
        if n in K:
            answer="GRESKA"
            break
        else:
            k-=1
            K.add(n)
    elif a=='H':
        if n in H:
            answer="GRESKA"
            break
        else:
            h-=1
            H.add(n)
    else:
        if n in T:
            answer="GRESKA"
            break
        else:
            t-=1
            T.add(n)

print(answer) if answer else print(p,k,h,t)
