#from collections import Counter
from collections import Counter

X = int(input())
sizes = list(map(int, input().split()))
inventory = Counter(sizes)

N = int(input())
earnings = 0

for _ in range(N):
    size, price = map(int, input().split())
    if inventory[size] > 0:
        earnings += price
        inventory[size] -= 1

print(earnings)