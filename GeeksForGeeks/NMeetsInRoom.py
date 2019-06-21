# Problem Description: https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room/0
import operator


class Meeting:
    def __init__(self):
        self.start = None
        self.finish = None
        self.index = None


t = int(input())

for _ in range(t):
    n = int(input())
    S = [int(x) for x in input().split()]
    F = [int(x) for x in input().split()]

    meetings = []

    for i in range(n):
        meet = Meeting()
        meet.start = S[i]
        meet.finish = F[i]
        meet.index = i
        meetings.append(meet)

    meetings.sort(key=operator.attrgetter('finish'))

    i = 0
    print(meetings[i].index+1, end=" ")
    for j in range(1, n):
        if(meetings[j].start >= meetings[i].finish):
            print(meetings[j].index+1, end=" ")
            i = j

    print()
