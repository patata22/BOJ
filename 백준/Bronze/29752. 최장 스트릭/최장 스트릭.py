n=int(input())
number=tuple(map(int,input().split()))

answer=-float('inf')
streak=0
for i in range(n):
     if number[i]:
          streak+=1
     else:
          answer=max(answer,streak)
          streak=0
answer=max(answer,streak)
print(answer)
          
