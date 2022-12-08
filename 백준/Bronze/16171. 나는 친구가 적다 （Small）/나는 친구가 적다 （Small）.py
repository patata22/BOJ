w=""
for x in input():
    if 48<=ord(x)<=57: continue
    w+=x
print('01'[input() in w])