#Iterables and Iterators
from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

total = list(combinations(letters, k))
count = 0

for c in total:
    if 'a' in c:
        count += 1

print(count / len(total))