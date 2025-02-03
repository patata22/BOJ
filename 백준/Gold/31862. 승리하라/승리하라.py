import sys
input=sys.stdin.readline


def sol(depth,maxScore, maxCnt):
   if depth==N:
      global answer
      if maxCnt==1 and maxScore==score[k]: answer+=1
      return

   for x in game[depth]:
      score[x]+=1
      if score[x]>maxScore:sol(depth+1, score[x],1)
      elif score[x]==maxScore: sol(depth+1, maxScore,maxCnt+1)
      else: sol(depth+1, maxScore,maxCnt)
      score[x]-=1

n,m,k=map(int,input().split())
score=[0]*(n+1)
game=[]
for _ in range(m):
   a,b,c=map(int,input().split())
   if c==0: game.append((a,b))
   elif c==1: score[a]+=1
   else: score[b]+=1
N=len(game)

maxScore = max(score)
maxCnt=score.count(maxScore)
answer=0

sol(0,maxScore,maxCnt)

print(answer)