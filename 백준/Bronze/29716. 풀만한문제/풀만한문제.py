def sol(s):
    total=0
    for x in s:
        if x==' ': total+=1
        elif x.isupper(): total+=4
        else:total+=2
    if total<=j: return 1
    return 0

j,n=map(int,input().split())
answer=0
for _ in range(n):
    answer+=sol(input())
print(answer)
