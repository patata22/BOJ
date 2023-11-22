for _ in range(int(input())):
    a,b,c=map(float,input().split())
    d=(b*b-4*a*c)**0.5
    print('%.3f, %.3f' %((-b+d)/(2*a),(-b-d)/(2*a)))
    