while True:
    x,y,z=map(float,input().split())
    if not x: break
    answer=[]
    if x<=4.5 and y>=150 and z>=200: answer.append("Wide Receiver")
    if x<=6.0 and y>=300 and z>=500: answer.append("Lineman")
    if x<=5.0 and y>=200 and z>=300: answer.append("Quarterback")
    if not answer: print("No positions")
    else: print(*answer)
