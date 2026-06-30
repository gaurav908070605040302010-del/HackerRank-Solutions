#Company Logo
from collections import Counter

s = input()

count = Counter(s)

result = sorted(count.items(), key=lambda x: (-x[1], x[0]))

for ch, freq in result[:3]:
    print(ch, freq)