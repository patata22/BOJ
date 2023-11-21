a1,a2,a3,b1,b2,b3,l=map(int,input().split())
if a1*b1+a2*b2+a3*b3<l: print(0)
else:   
    use=[[a1,b1],[a2,b2],[a3,b3]]
    use.sort(key=lambda x: x[0])
    answer=0
    while l>0:
        l-=use[-1][0]
        use[-1][1]-=1
        if not use[-1][1]:use.pop()
        answer+=1
    print(answer)
