src = input()
result = []
stack = []
for it in src:
    if it == ' ' and '<' not in stack:
        stack.reverse()
        stack.append(it)
        result += stack
        stack = []
    elif it == '>':
        stack.append(it)
        result += stack
        stack = []
    elif it == '<':
        stack.reverse()
        result += stack
        stack = [it]
    else:
        stack.append(it)
if len(stack) != 0:
    stack.reverse()
    result += stack
for it in result:
    print(it,end='')