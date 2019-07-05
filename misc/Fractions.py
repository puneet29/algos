# Problem: Given an array of integers, calculate which fraction
# of its elements are positive, which fraction of its elements
# are negative, and which fraction of its elements are zeroes,
# respectively. Print the decimal value of each fraction on a new line.

inp = [int(x) for x in input().split()]
n = inp[0]
arr = inp[1:]
pos = 0
neg = 0
zero = 0

for num in arr:
    if(num < 0):
        neg += 1
    elif(num > 0):
        pos += 1
    else:
        zero += 1

pos /= n
neg /= n
zero /= n

print('{0:.6f}'.format(pos))
print('{0:.6f}'.format(neg))
print('{0:.6f}'.format(zero))
