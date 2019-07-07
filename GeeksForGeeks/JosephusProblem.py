# Problem Description: https://practice.geeksforgeeks.org/problems/josephus-problem/1

import math


def josephus(n, k):
    if(n == 1):
        return 1

    return((josephus(n-1, k)+k-1) % n+1)


def main():

    T = int(input())

    while(T > 0):

        nk = [int(x) for x in input().strip().split()]
        n = nk[0]
        k = nk[1]

        print(josephus(n, k))

        T -= 1


if __name__ == "__main__":
    main()
