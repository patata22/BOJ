SIZE=62*30000
t=0
while True:
    n=int(input())
    if not n: break
    if t: print()
    t+=1
    n=(n+1)//2
    n+=(n+1)//2
    answer= (n+SIZE-1)//SIZE
    print(f'File #{t}\nJohn needs {answer} floppies.')