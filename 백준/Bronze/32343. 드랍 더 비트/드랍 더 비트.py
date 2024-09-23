n=int(input())
x,y=map(int,input().split())
gap=max(x+y-n,0)
answer=['0']*n
for i in range(x+y-2*gap):
    answer[i]='1'
print(int(''.join(answer),2))
