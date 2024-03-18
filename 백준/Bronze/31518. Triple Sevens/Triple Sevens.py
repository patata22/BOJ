input()
cnt=0
for _ in range(3):
    if 7 in map(int,input().split()):cnt+=1
if cnt==3:print(777)
else:print(0)
