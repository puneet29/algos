# Problem Description: https://practice.geeksforgeeks.org/problems/run-length-encoding/1


def encode(arr):
    cur = arr[0]
    output = ''
    count = 0

    for char in arr:
        if(char == cur):
            count += 1
        else:
            output += cur+str(count)
            count = 1
            cur = char
    output += cur+str(count)

    return output


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip()
        print(encode(arr))
