# Problem taken from CodeVita 8

n = int(input())
s = input()
q = int(input())
ps = []

for i in range(q):
    ps.append(int(input()))

arr = []

freq = {}
for i in range(n):
    if(s[i] in freq):
        freq[s[i]] += 1
    else:
        freq[s[i]] = 1
    arr.append(freq[s[i]] - 1)

for p in ps:
    print(arr[p-1])
