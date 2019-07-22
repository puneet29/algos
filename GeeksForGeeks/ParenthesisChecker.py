# Problem Description: https://practice.geeksforgeeks.org/problems/parenthesis-checker/0/

def matchParenthesis(a, b):
    if((a == '[' and b == ']') or (a == '(' and b == ')') or (a == '{' and b == '}')):
        return True
    return False


def checkParenthesis(s):
    stack = []

    for i in range(len(s)):
        if(s[i] == '(' or s[i] == '[' or s[i] == '{'):
            stack.append(s[i])
        elif((s[i] == ')' or s[i] == ']' or s[i] == '}') and len(stack)):
            if(not matchParenthesis(stack[-1], s[i])):
                return 'not balanced'
            stack.pop()
        else:
            return 'not balanced'
    if(len(stack)):
        return 'not balanced'
    return 'balanced'


t = int(input())
for _ in range(t):
    n = input()
    print(checkParenthesis(n))
