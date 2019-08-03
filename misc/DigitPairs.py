# Consider the pairs used in even places in odd places and vice-versa

def getBitScore(n):
    maxDigit = 0
    minDigit = 10
    while(n > 0):
        rem = n % 10
        n = n // 10
        if(rem > maxDigit):
            maxDigit = rem
        if(rem < minDigit):
            minDigit = rem
    score = maxDigit * 11 + minDigit * 7
    return int(str(score)[-2])


def getPairsUtil(n):
    if(n <= 1):
        return 0
    if(n == 2):
        return 1
    else:
        return 2


def getPairs(scores, start, end):

    indexNums = {}
    pairs = 0

    for i in range(start, end, 2):
        index = scores[i]
        if(index in indexNums):
            indexNums[index] += 1
        else:
            indexNums[index] = 1

    for index, freq in indexNums.items():
        pairs += getPairsUtil(freq)

    return pairs


if __name__ == "__main__":
    n = int(input())
    nums = [int(x) for x in input().split()]
    scores = []

    for i in nums:
        scores.append(getBitScore(i))

    pairs = getPairs(scores, 0, n)
    pairs += getPairs(scores, 1, n)

    print(pairs)
