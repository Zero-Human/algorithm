# (()[[]])([])

stack = []
src = input()
count = 0
swap = [0] * 30
for it in src:
    if len(stack) == 0 and (it == ')' or it == ']'):
        swap[0]= 0
        break
    else: 
        if it == ')':
            if stack[-1][1] == '[':
                swap[0]= 0
                break
            else:
                index, value = stack.pop()
                if swap[index+1] == 0:
                    swap[index] += 2
                else:
                    swap[index] += 2* swap[index+1]
                    swap[index+1] = 0
                count -=1

        elif it == ']':
            if stack[-1][1] == '(':
                swap[0]= 0
                break
            else:
                index, value = stack.pop()
                if swap[index+1] == 0:
                    swap[index] += 3
                else:
                    swap[index] += 3* swap[index+1]
                    swap[index+1] = 0
                count -=1
        else:
            stack.append((count,it))
            count +=1
print(swap[0])