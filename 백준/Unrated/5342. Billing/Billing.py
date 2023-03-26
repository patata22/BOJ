price={'Paper':57.99, 'Printer': 120.50, 'Planners':31.25, 'Binders':22.50, 'Calendar':10.95, 'Notebooks':11.20, 'Ink':66.95}
answer=0
while True:
    x=input()
    if x=='EOI':
        print(f'${answer}')
        break
    else: answer+=price[x]