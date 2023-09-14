weight=0
price=0
for _ in range(int(input())):
    t,w,h,l = input().split()
    w=int(w)
    h=int(h)
    l=int(l)
    if t=='A':
        apple = (w//12)*(h//12)*(l//12)
        weight+= 500*apple+1000
        price+= 4000*apple
    else:
        weight+=6000
print(weight)
print(price)
        
