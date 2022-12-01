num = int(input())
queue = [it for it in range(1,num+1)]
while queue:
    print(queue.pop(0),end=' ')
    if queue:
        value = queue.pop(0)
        queue.append(value)