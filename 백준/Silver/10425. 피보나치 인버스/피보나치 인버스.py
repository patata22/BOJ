answer={}
answer[1]=2
a,b=1,1
for i in range(3,100001):
    a,b=b,a+b
    answer[b]=i

for _ in range(int(input())):
    print(answer[int(input())])
