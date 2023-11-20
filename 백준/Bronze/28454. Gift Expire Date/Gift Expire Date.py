coupon=[(input(),1)]
n=int(input())
for _ in range(n):
    coupon.append((input(),0))
coupon.sort(key=lambda x: x[0])
for i in range(n+1):
    if coupon[i][1]:
        print(n-i)
        break