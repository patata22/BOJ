d={136:1,142:5,148:10,154:50}
answer=0
for _ in range(int(input())):
    a,b=map(int,input().split())
    answer+=d[a]
print(1000*answer)

