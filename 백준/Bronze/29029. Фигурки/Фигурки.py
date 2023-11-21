c={'N':0,'S':1,'W':2,'E':3}
count=[0]*4
n=int(input())
for x in input():
    count[c[x]]+=1
print(n-max(count))