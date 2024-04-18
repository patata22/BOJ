answer={}
temp=""
for i in range(1,10):
    temp+=str(i)
    answer[temp]=i

x=input()
if x in answer:print(answer[x])
else:print(-1)
