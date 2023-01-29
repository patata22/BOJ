input()
q=0
a=0
while True:
    x=input()
    if len(x.split())==3: break
    if x=='문제':q+=1
    else:
        if q<=a:q+=2
        else:a+=1

print("고무오리야 사랑해") if q<=a else print("힝구")

