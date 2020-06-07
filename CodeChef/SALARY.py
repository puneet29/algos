def endCase(w):
    for i in w[1:]:
        if i != w[0]:
            return False
    return True


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        w = [int(i) for i in input().split()]
        passes = 0
        wMax = max(w)
        while not endCase(w):
            passedMax = False
            for i in range(n):
                if w[i] == wMax and not passedMax:
                    passedMax = True
                    continue
                elif w[i] == wMax and passedMax:
                    wMax = w[i] + 1
                w[i] += 1

            passes += 1
        print(passes)
