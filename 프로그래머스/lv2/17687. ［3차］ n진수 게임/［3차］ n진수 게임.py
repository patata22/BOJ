def solution(n, t, m, p):
    p-=1
    answer = ''
    record={10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    for i in range(10):
        record[i]=str(i)
    
    future="0"
    now=1
    while len(future)<m*t:
        future+=change(now,n,record)
        now+=1
    print(future)
    for i in range(p, m*t, m):
        answer+=future[i]
    
    return answer

def change(number, n,record):
    temp=""
    while number:
        temp+=record[number%n]
        number//=n
    return temp[::-1]
    

    