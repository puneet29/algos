rate = float(input())/100
R = int(input())
txn = []
amount = [0 for i in range(R)]
cred = ['' for i in range(R)]
bal = [0 for i in range(R)]
interest = [0 for i in range(R)]
miss = -1

for i in range(R-2):
    a = [x for x in input().split()]
    txn.append(int(a[0]))
    amount[txn[i]-1] = int(a[1])
    cred[txn[i]-1] = a[2]
    bal[txn[i]-1] = int(a[3])
    interest[txn[i]-1] = bal[txn[i]-1]*rate/365

total_interest = float(input())

for i in reversed(range(R)):
    if(not bal[i]):
        miss = i
        break

if(cred[miss+1] == 'debit'):
    bal[miss] = bal[miss+1] + amount[miss+1]
else:
    bal[miss] = bal[miss+1] - amount[miss+1]

interest[miss] = bal[miss]*rate/365
interest[miss-1] = total_interest - sum(interest)

bal[miss-1] = round(interest[miss-1] * 365 / rate)

for i in range(miss-1, miss+1):
    if(bal[i]-bal[i-1]>=0):
        cred[i] = 'credit'
        amount[i] = bal[i] - bal[i-1]
        txn.append(i+1)
    else:
        cred[i] = 'debit'
        amount[i] = bal[i-1] - bal[i]
        txn.append(i+1)

print(txn[-2], amount[miss-1], cred[miss-1], bal[miss-1])
print(txn[-1], amount[miss], cred[miss], bal[miss])
