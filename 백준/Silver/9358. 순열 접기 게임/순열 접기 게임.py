for t in range(1,int(input())+1):
     input()
     number=list(map(int,input().split()))
     while len(number)>2:
          l=len(number)
          nxt=[]
          if l%2:
               for i in range(l//2):
                    nxt.append(number[i]+number[l-1-i])
               nxt.append(number[l//2]*2)
          else:
               for i in range(l//2):
                    nxt.append(number[i]+number[l-1-i])
          number=nxt
          
               
     if number[0]>number[1]:print(f'Case #{t}: Alice')
     else: print(f'Case #{t}: Bob')
     
