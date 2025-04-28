import sys
input=sys.stdin.readline

def sol():
    now=1
    response=0
    while True:
        print('?',now,flush=True)
        response=int(input())
        if response==0: return now
        elif response==now: now<<=1
        else: return now-response

print('!',sol())