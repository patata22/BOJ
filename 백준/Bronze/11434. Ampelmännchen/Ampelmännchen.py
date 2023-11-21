for t in range(int(input())):
    if t: print()
    n,w,e=map(int,input().split())
    answer=0
    for _ in range(n):
        a,b,c,d=map(int,input().split())
        answer+=max(w*a+c*e, b*w+d*e)
    print(f'Data Set {t+1}:\n{answer}')
    
