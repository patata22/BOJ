def choice(now):
    if now==n:
        result.add(sum(chosen))
        return
    chosen.append(number[now])
    choice(now+1)
    chosen.pop()
    choice(now+1)
        
n=int(input())
number=sorted(map(int,input().split()))
chosen=[]
result=set()

choice(0)

for i in range(1,2000002):
    if i not in result:
        print(i)
        break
  