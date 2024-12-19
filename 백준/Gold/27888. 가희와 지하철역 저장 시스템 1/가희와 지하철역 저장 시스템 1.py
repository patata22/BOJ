import sys
input=sys.stdin.readline

def calc(feat):
    result=0
    for x in feat:
        if x not in featureToNum: return -1
        result|=1<<featureToNum[x]
    return result

station={}
featureToNum={}
unused=0
for _ in range(int(input())):
    name=input().rstrip()
    station[name]=0
count=[0]*1024
for _ in range(int(input())):
    temp=input().rstrip().split()
    cmd=temp[0]
    if cmd=='U':
        name=temp[1]
        features=temp[2].split(',')
        for x in features:
            if x not in featureToNum:
                featureToNum[x]=unused
                unused+=1
        now=station[name]
        for i in range(1,1024):
            if i&now==i: count[i]-=1
        value=calc(features)
        station[name]=value
        for i in range(1,1024):
            if i&value==i:                
                count[i]+=1
    else:
        features=temp[1].split(',')
        result=calc(features)
        if result==-1: print(0)
        else:  print(count[result])
