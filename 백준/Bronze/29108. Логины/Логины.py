answer='Correct'
x=input()
if len(x)<3:answer='Incorrect'
if x[:2]!='io': answer='Incorrect'
for y in x[2:]:
    if not y.isdigit():answer='Incorrect'
print(answer)
