temp=input().rstrip(')').split('(')
print(temp[0].rstrip())
if len(temp)==1:print('-')
else: print(temp[1])
