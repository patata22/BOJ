def sol(q,w,e,x):
    if x<0: return
    answer.append((q,w,e))
    sol(q+1,w,e,x-a)
    sol(q,w+1,e,x-b)
    sol(q,w,e+1,x-c)
      
a,b,c,n=[int(input()) for i in range(4)]

answer=0

for i in range(0,101):
    for j in range(0,101):
        for k in range(0,101):
            if i==j==k==0: continue
            if a*i+b*j+c*k<=n:
                print(f'{i} Brown Trout, {j} Northern Pike, {k} Yellow Pickerel')
                answer+=1
print(f'Number of ways to catch fish: {answer}')