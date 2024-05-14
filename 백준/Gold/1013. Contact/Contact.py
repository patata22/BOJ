import re
reg=re.compile('(100+1+|01)+')
for tt in range(int(input())):
    signal=input()
    if reg.fullmatch(signal):print('YES')
    else:print('NO')
