s = input()
k = 1

while(not s.startswith('-')):
    stack = []
    operations = 0
    for i in s:
        if i == '{':
            stack.append('{')
        elif i == '}':
            if len(stack) == 0:
                operations += 1
                stack.append('{')
            else:
                stack.pop()
    if len(stack) != 0:
        operations += len(stack) // 2

    print(f'{k}. {operations}')

    s = input()
    k += 1
