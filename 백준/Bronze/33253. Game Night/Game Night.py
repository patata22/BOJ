n=int(input())
origin=[0]*26
for x in input():
   origin[ord(x)-97]+=1
for x in input():
   origin[ord(x)-97]-=1
answer=0
for x in origin:
   if x>0: answer+=x
print(answer)
