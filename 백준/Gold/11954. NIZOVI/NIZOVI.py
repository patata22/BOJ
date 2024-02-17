def parse():
    idx=-1
    depth=0
    temp=[]
    while idx<n-1:
        idx+=1
        if data[idx]=='{':
            print(' '*2*depth+'{')
            depth+=1
        elif data[idx]=='}':
            if temp: print(' '*2*depth+''.join(temp))
            temp=[]
            depth-=1
            if idx+1<n and data[idx+1]==',':
                idx+=1
                print(' '*2*depth+'},')
            else: print(' '*2*depth+'}')
        elif data[idx]==',':
            if temp:
                print(' '*2*depth+''.join(temp),end='')
                temp=[]
            print(',')
        else: temp.append(data[idx])
        
data=list(input())
n=len(data)
answer=[]
parse()
