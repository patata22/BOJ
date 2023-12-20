
while True:
    a,b=map(int,input().split())
    if not a: break
    b=min(a-b,b)
    answer=1
    for i in range(a,a-b,-1):
        answer*=i
    for i in range(2,b+1): answer//=i
    print(answer)
