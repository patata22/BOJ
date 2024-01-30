input()
number=list(map(int,input().split()))
answer=0
for x in number: answer^=x
if not answer: print('cubelover')
else:print('koosaga')
