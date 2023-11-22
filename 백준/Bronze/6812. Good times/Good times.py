add=[('Ottawa',0),('Victoria',-180),('Edmonton',-120),('Winnipeg',-60),('Toronto',0),('Halifax',60),("St. John's",90)]

t=int(input())
total=60*(t//100)+t%100
for n,x in add:
    T=(total+x)%1440
    h=T//60
    m=T%60
    print(f'{100*h+m} in {n}')