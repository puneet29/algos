# Problem Description: https://practice.geeksforgeeks.org/problems/convert-time-from-12-hour-to-24-hour-format/0

testcases = int(input())

for _ in range(testcases):
    t = input()

    if(t[:2] == '12'):
        if(t[-2:] == 'AM'):
            print('00'+t[2:len(t)-2])
        else:
            print('12'+t[2:len(t)-2])
    else:
        if(t[-2:] == 'AM'):
            print(t[:len(t)-2])
        else:
            h = str(int(t[:2]) + 12)
            print(h+t[2:len(t)-2])
