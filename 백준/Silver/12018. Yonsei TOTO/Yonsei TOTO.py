n,m=map(int,input().split())
final=[]
for _ in range(n):
    p,l=map(int,input().split())
    number=sorted(list(map(int,input().split())), reverse=True)
    if l>p: final.append(1)
    else: final.append(number[l-1])
final.sort()
answer=0
for x in final:
    if x>m: break
    else:
        m-=x
        answer+=1
print(answer)
   