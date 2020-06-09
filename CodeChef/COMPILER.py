t = int(input())

for _ in range(t):
    exp = input()
    stack = []
    ans = 0
    out = 0

    for i in exp:
        if i == '<':
            stack.append("<")
        elif i == '>':
            if len(stack) > 0:
                stack.pop()
                ans += 2
                if len(stack) == 0:
                    out = ans
            else:
                break

    print(out)
