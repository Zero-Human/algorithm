count, num = map(int,input().split())
lists = [it for it in range(1,count+1)]
swap_count = 0
result=[]
while lists:
    value = lists.pop(0)
    swap_count +=1
    if swap_count == num:
        swap_count = 0
        result.append(value)
    else:
        lists.append(value)


print('<',end='')
for it in result:
    if it == result[-1]:
        print(it,end='')
    else:    
        print(it, end=', ')
print('>')