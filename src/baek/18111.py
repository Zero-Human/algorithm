
import sys
input = sys.stdin.readline
row, col, inven = map(int,input().split())
mark_map = [list(map(int,input().split())) for _ in range(row)]
result = [1e9,267]
for it in range(min(map(min, mark_map)),max(map(max, mark_map))+1):
    swap_inven = inven
    time = 0
    for it2 in mark_map:
        for it3 in it2:
            value = abs(it-it3)
            if it3 < it:
                time += value
                swap_inven-= value
            elif it3> it:
                time += value * 2
                swap_inven += value
    if swap_inven >= 0 and it <= 256 and it >= 0:
        result = [time,it] if result[0] >= time else result
print(result[0],result[1])