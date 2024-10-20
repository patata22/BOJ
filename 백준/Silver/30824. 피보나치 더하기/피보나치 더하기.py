fibo=[1,1]
while fibo[-1]+fibo[-2]<10**16:
    fibo.append(fibo[-1]+fibo[-2])

one=set()
two=set()
three=set()
for i in range(78):
    one.add(fibo[i])
    for j in range(78):
        two.add(fibo[i]+fibo[j])
        for k in range(78):
            three.add(fibo[i]+fibo[j]+fibo[k])

answer=[0,one,two,three]
for _ in range(int(input())):
    a,b=map(int,input().split())
    print('YES') if b in answer[a] else print('NO')
