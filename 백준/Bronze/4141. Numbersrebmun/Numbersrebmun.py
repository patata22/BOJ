def change(x):
    if x in 'abc': return '2'
    elif x in 'def': return '3'
    elif x in 'ghi': return '4'
    elif x in 'jkl': return '5'
    elif x in 'mno': return '6'
    elif x in 'pqrs': return '7'
    elif x in 'tuv': return '8'
    return '9'
    

for _ in range(int(input())):
    temp=list(map(lambda x: change(x.lower()), input()))
    if temp==temp[::-1]: print('YES')
    else:print('NO')
