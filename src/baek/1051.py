row, col = map(int,input().split())
src = []
min_count = row if row < col else col
result = []
for it in range(row):
    src.append([int(el) for el in input()])

for i in range(row):
    for j in range(col):
        for it in range(min_count):
            if i+it > row-1 or j + it > col-1 :
                break
            if src[i][j] == src[i][j+it] == src[i+it][j] == src[i+it][j+it]:
                result.append((it+1)*(it+1))
print(max(result))