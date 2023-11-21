v='aeiou'
answer=1
X=input()
for i in range(len(X)-1):
    if X[i] in v and X[i+1] in v: answer=0
    if X[i] not in v and X[i+1] not in v:  answer=0
print(answer)
    
