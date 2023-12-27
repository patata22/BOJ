import datetime

while True:
    d,m,y=map(int,input().split())
    if not d: break
    dt1=datetime.datetime(y,1,1)
    dt2=datetime.datetime(y,m,d)
    t=dt2-dt1
    print(t.days+1)
