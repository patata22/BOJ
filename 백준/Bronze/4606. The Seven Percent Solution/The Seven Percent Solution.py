record={}
record[' ']='%20'
record['!']='%21'
record['$']='%24'
record['%']='%25'
record['(']='%28'
record[')']='%29'
record['*']='%2a'
def change(x):
    if x in record: return record[x]
    return x

while True:
    x=''.join(list(map(lambda x: change(x), input())))
    if x[0]=='#': break
    print(x)
    
    
    
