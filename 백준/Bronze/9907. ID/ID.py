Map={0:'J',1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'Z'}
weight=[2,7,6,5,4,3,2]
total = 0
id=list(input())
for i in range(7):
    total+=int(id[i])*weight[i]
print(Map[total%11])
