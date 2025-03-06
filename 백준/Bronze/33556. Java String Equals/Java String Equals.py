def equals(a,b):
    if a=='null': return 'NullPointerException'
    if a==b: return 'true'
    else: return 'false'

def ignore(a,b):
    if a=='null': return 'NullPointerException'
    if b=='null': return 'false'
    if a.lower()==b.lower(): return 'true'
    else: return 'false'

a,b=input(),input()
print(equals(a,b))
print(ignore(a,b))


    
