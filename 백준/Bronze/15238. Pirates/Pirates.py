cnt={}
for _ in range(97,123): cnt[chr(_)]=0
input()
for x in input():cnt[x]+=1
a=0
b=0
for x in cnt:
    if cnt[x]>a:
        a=cnt[x]
        b=x
print(b,a)