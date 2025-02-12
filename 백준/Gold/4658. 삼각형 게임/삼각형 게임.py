def sol(depth):
   if depth==6:
      global answer
      total=sum(bottom)
      answer=max(answer,total)
      return
   elif depth==5:
      for i in range(1,6):
         if not used[i]:
            used[i]=1
            now=triangle[i][:]
            for j in range(3):
               if now[0]==right[0] and now[1]==left[depth-1]:
                  left[5]=now[0]
                  right[5]=now[1]
                  bottom[5]=now[2]
                  sol(depth+1)
               now.append(now.pop(0))
            used[i]=0
      return
      
   for i in range(1,6):
      if not used[i]:
         used[i]=1
         now=triangle[i][:]
         for j in range(3):
            if now[1]==left[depth-1]:
               left[depth]=now[0]
               right[depth]=now[1]
               bottom[depth]=now[2]
               sol(depth+1)
            now.append(now.pop(0))
         used[i]=0

while True:
   left=[0]*6
   right=[0]*6
   bottom=[0]*6
   triangle=[list(map(int,input().split())) for i in range(6)]
   used=[0]*6
   used[0]=1
   answer=0
   now=triangle[0][:]
   for i in range(3):
      left[0]=now[0]
      right[0]=now[1]
      bottom[0]=now[2]
      sol(1)
      now.append(now.pop(0))
   if not answer: print('none')
   else: print(answer)
   if input()=='$': break
