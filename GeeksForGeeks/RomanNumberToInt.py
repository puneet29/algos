# Problem Description: https://practice.geeksforgeeks.org/problems/roman-number-to-integer/0/

def strength(a):
    if(a == 'I'):
        return 1
    if(a == 'V'):
        return 5
    if(a == 'X'):
        return 10
    if(a == 'L'):
        return 50
    if(a == 'C'):
        return 100
    if(a == 'D'):
        return 500
    if(a == 'M'):
        return 1000


def romanToInt(r):
    equiInt = strength(r[-1])

    for i in reversed(range(len(r)-1)):
        if(strength(r[i+1]) > strength(r[i])):
            equiInt -= strength(r[i])
        else:
            equiInt += strength(r[i])
    return(equiInt)


t = int(input())

for _ in range(t):
    roman = input()
    print(romanToInt(roman))
