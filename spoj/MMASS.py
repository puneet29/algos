formula = input()
MMASS = {'H': 1, 'C': 12, 'O': 16}
nums = [str(i) for i in range(2, 10)]
stack = []

for i in range(len(formula)):
    if formula[i] in ['H', 'C', 'O']:
        stack.append(MMASS[formula[i]])
    elif formula[i] == '(':
        stack.append('(')
    elif formula[i] in nums:
        item = stack.pop()
        stack.append(item*int(formula[i]))
    elif formula[i] == ')':
        item = stack.pop()
        ans = 0
        while(item != '('):
            ans += item
            item = stack.pop()
        stack.append(ans)
print(sum(stack))
