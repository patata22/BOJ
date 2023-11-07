a,b=map(int,input().split())

answer = a*b/24200
if answer==int(answer):print(int(answer))
else: print(int(answer)+1)
