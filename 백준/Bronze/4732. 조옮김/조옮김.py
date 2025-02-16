def sol():
   answer=[]
   n=int(input())
   for x in temp:
      tmp=score[x[0]]
      if len(x)==2:
         if x[-1]=='#': tmp+=1
         else: tmp-=1
      answer.append(reverse[(tmp+n)%12])
   return answer

score={'A':0, 'B':2, 'C':3, 'D':5, 'E':7,'F':8,'G':10}
reverse={}
for x in score:
   reverse[score[x]]=x
reverse[1]='A#'
reverse[4]='C#'
reverse[6]='D#'
reverse[9]='F#'
reverse[11]='G#'

while True:
   temp=input().split()
   if temp[0]=='***': break
   print(*sol())
