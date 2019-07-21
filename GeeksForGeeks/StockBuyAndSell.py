# Problem Description: https://practice.geeksforgeeks.org/problems/stock-buy-and-sell/0


def printBuySell(a, n):
    buy = 0
    prev = 0
    sell = 0
    i = 0
    res = []
    for i in range(n):
        if(a[prev] <= a[i] and i != n-1):
            prev = i
            sell = i
        else:
            if(i == n-1 and a[prev] <= a[i]):
                sell = n-1
            if(sell != 0):
                res.append('({0} {1})'.format(buy, sell))
            buy = i
            prev = buy
            sell = 0

    return res


t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    res = printBuySell(a, n)
    if(len(res) > 0):
        print(' '.join(res))
    else:
        print('No Profit')
