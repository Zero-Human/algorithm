count = int(input())
for _ in range(count):
    print_count, index = map(int,input().split())
    lists = list(map(int,input().split()))
    result = 0
    target = index
    while lists:
        value = lists.pop(0)
        target -=1
        if len(lists) == 0 or max(lists) <= value:
            result+=1
        else:
            lists.append(value)
            if target == -1:
                target = len(lists) - 1
        if target == -1:
            print(result)

