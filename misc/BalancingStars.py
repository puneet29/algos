# Problem taken from TCS Codevita


def match(b2, b1):
    if((b1 == '(' and b2 == ')') or (b1 == '[' and b2 == ']') or (b1 == '{' and b2 == '}')):
        return True
    return False


if __name__ == "__main__":
    s = input()
    stack = ['$']
    balanced = 0
    stars = 'Yes'
    startbrace = ['(', '[', '{']
    endbrace = [']', ')', '}']

    for i in s:
        if(i in startbrace):
            stack.append(i)
        elif(i in endbrace):
            count = 0
            if(len(stack)>1):
                brace = stack.pop()
            else:
                brace = ''
            while(brace == '*' and len(stack)>1):
                count += 1
                brace = stack.pop()
            if(stars=='Yes'):
                if(count < 2):
                    stars = 'No'
            if(match(i, brace)):
                balanced += 1
        if(i == '*'):
            if(stack[-1] in startbrace+['*']):
                stack.append(i)

    print(stars, balanced)
