temp=list(input())
origin=""
for x in temp:
    if 48<=ord(x)<=57: continue
    origin+=x

target=input()
if target in origin:print(1)
else:print(0)
