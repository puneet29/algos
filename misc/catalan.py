n = int(input('Enter the index to generate catalan number: '))
catalan = [1]

for i in range(1, n):
    catalanTemp = 0
    for j in range(i):
        catalanTemp += catalan[j] * catalan[i-j-1] 
    catalan.append(catalanTemp)

print(catalan)