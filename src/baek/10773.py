
count = int(input())
stack = []
for _ in range(count):
    value = int(input())
    if len(stack) != 0 and value == 0:
        stack.pop()
    elif value != 0:
        stack.append(value)
print(sum(stack))