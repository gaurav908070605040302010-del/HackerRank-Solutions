#Maximize It!
from itertools import product

K, M = map(int, input().split())

lists = []
for _ in range(K):
    lists.append(list(map(int, input().split()))[1:])

ans = 0
for p in product(*lists):
    ans = max(ans, sum(x**2 for x in p) % M)

print(ans)