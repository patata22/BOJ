x=input()
if len(x)>2 and x[0]=='"' and x[-1]=='"':print(x.strip('"'))
else:print('CE')
