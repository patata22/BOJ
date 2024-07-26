x=""" @@@   @@@ 
@   @ @   @
@    @    @
@         @
 @       @ 
  @     @  
   @   @   
    @ @    
     @     """
x=x.split('\n')
n=int(input())

answer=[[] for i in range(9)]
for i in range(9):
    for j in range(n):
        answer[i].append(x[i])

for i in range(9):
    print(*answer[i])

    
