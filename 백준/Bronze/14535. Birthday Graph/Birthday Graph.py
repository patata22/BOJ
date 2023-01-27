month=["","Jan", "Feb", "Mar", 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
case=0
while True:
    case+=1
    n=int(input())
    if not n: break
    count=[0]*13
    for i in range(n):
        a,b,c = map(int,input().split())
        count[b]+=1

    print(f'Case #{case}:')
    for i in range(1,13):
        print(f'{month[i]}:{"*"*count[i]}')
