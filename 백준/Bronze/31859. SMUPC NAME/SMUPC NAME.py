n,s=input().split()
temp=[]
n=int(n)
se=set()
count=0
for x in s:
    if x in se:  count+=1
    else:
        temp.append(x)
        se.add(x)

print("smupc_"+(str(n+1906)+''.join(temp)+str(count+4))[::-1])
