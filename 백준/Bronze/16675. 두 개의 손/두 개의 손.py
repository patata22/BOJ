win={'R':'P', 'S':'R', 'P':'S'}
a,b,c,d=input().split()
if a==b and win[a] in (c,d):print("TK")
elif c==d and win[c] in (a,b):print("MS")
else: print("?")