number = input()
numbers = [it for it in range(10)]
swap = numbers[:]
result = 1
for it in number:
    value = int(it)
    if value in swap:
        del swap[swap.index(value)]
    else:
        if value == 9 and  6 in swap:
            del swap[swap.index(6)]
        elif value == 6  and  9 in swap:
            del swap[swap.index(9)]
        else:
            result += 1
            swap += numbers
            del swap[swap.index(value)]
print(result)
            