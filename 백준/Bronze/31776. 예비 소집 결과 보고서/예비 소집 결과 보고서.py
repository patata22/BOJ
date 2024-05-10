def parse(x):
    if x=='-1':return float('inf')
    else: return int(x)

answer=0
for _ in range(int(input())):
    temp=list(map(parse,input().split()))
    so=sorted(temp)
    if so[0]!=float('inf') and temp==so:
        answer+=1
print(answer)
