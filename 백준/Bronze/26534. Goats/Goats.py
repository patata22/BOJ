number1=list(map(int,input().split()))
number2=list(map(int,input().split()))
total=0
win=0
for x in number1:
    for y in number2:
        if x!=y:total+=1
        if x>y: win+=1
print('%.5f' %round(win/total,5))
