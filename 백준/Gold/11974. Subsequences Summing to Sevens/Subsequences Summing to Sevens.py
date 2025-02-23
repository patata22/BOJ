import sys
input=sys.stdin.readline

left=[0]*7
right=[0]*7
number=[0]
for i in range(1,int(input())+1):
   x=int(input())
   nxt=(x+number[-1])%7
   if not left[nxt]:left[nxt]=i
   right[nxt]=i
   number.append(nxt)
left[0]=0

answer=0
for i in range(7):
   answer=max(answer,right[i]-left[i])
print(answer)