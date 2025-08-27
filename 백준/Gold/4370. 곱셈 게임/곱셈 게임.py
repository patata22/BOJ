def sol():
    n=int(input())
    p=1
    while True:
        p*=9
        if p>=n:return 'Baekjoon wins.'
        p*=2
        if p>=n:return 'Donghyuk wins.'
    
while True:
    try:print(sol())
    except: break
