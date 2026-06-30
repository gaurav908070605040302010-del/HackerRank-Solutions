#Collections.OrderedDict()
from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    line = input().split()
    price = int(line[-1])
    item = " ".join(line[:-1])

    if item in items:
        items[item] += price
    else:
        items[item] = price

for item, total in items.items():
    print(item, total)