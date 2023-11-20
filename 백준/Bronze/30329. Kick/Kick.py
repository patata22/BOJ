temp=input()
n=len(temp)
answer=0
for i in range(n-3):
    if temp[i:i+4]=='kick':answer+=1
print(answer)
