a,b,c=map(int,input().split())
answer=0
for i in range(a,b+1):
    answer+=str(i).count(str(c))
print(answer)
