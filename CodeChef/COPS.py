t = int(input())

for _ in range(t):
    m, x, y = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    maxHouses = x * y
    houses = [1 for i in range(1, 101)]

    for house in c:
        lower = house - maxHouses
        lower = lower if lower > 0 else 1
        upper = house + maxHouses
        upper = upper if upper < 101 else 100
        houses[lower-1:upper] = [0 for i in range(upper+1-lower)]

    print(sum(houses))
