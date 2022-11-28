count = int(input())
swap = [False for it in range(21)]
for _ in range(count):
    func = list(map(str,input().split()))
    value = int(func[1]) if len(func) == 2 else 0
    func = func[0]
    if func == 'add':
            swap[value] = True
    elif func == 'remove':
            swap[value] = False
    elif func == 'check':
        if swap[value] == True:
            print(1)
        else:
            print(0)
    elif func == 'toggle':
        if swap[value] == True:
            swap[value] = False
        else:
            swap[value] = True
    elif func == 'all':
        swap = [True for it in range(21)]
    elif func == 'empty':
        swap = [False for it in range(21)]
