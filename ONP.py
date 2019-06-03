def priority(op):
    if(op == "^"):
        return 5
    elif(op == "/"):
        return 4
    elif(op == "*"):
        return 3
    elif(op == "-"):
        return 2
    elif(op == "+"):
        return 1
    else:
        return 0


t = int(input())
for i in range(t):
    exp = input()
    stck = []
    res = []
    for token in exp:
        if(token == "("):
            stck.append("(")
        elif(token == ")"):
            temp = stck.pop()
            while(temp != "("):
                res.append(temp)
                temp = stck.pop()
        elif((token >= "a" and token <= "z") or
             (token >= "A" and token <= "Z")):
            res.append(token)
        else:
            if(priority(stck[-1]) <= priority(token)):
                stck.append(token)
            else:
                res.append(stck.pop())
                stck.append(token)
    print("".join(res))
