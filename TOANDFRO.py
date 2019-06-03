n = int(input())
while(n != 0):
    encrypt = input()
    decrypt = []
    for i in range(len(encrypt)//n):
        if(i % 2 == 0):
            decrypt.append([encrypt[n*i:n*i+n]])
        else:
            decrypt.append([encrypt[n*i-1+n:n*i-1:-1]])
    for i in range(n):
        for j in range(len(decrypt)):
            print(decrypt[j][0][i], end="")
    print()
    n = int(input())
