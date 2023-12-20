a=input()
countA={}
for x in a:
    if x not in countA:
        countA[x]=0
    countA[x]+=1
b=input()
countB={'*':0}
for x in b:
    if x not in countB:
        countB[x]=0
    countB[x]+=1

wild=countB['*']
diff=0
for x in countA:
    if x not in countB:diff+=countA[x]
    else:
        temp=max(countA[x]-countB[x],0)
        diff+=max(countA[x]-countB[x],0)
if diff>wild:print('N')
else:print('A')
