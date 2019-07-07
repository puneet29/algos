# Problem Description: https://practice.geeksforgeeks.org/problems/occurences-of-2-as-a-digit/1

def numberOf2s(n):
    n = str(n)
    count = 0
    for i in n:
        if(i == '2'):
            count += 1
    return count


def numberOf2sinRange(n):
    ans = 0
    for i in range(n+1):
        ans += numberOf2s(i)
    return ans


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(numberOf2sinRange(n))
