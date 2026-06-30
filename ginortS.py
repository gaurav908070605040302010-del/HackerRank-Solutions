#ginortS
s = input()

lower = sorted([c for c in s if c.isalpha() and c.islower()])
upper = sorted([c for c in s if c.isalpha() and c.isupper()])
odd = sorted([c for c in s if c.isdigit() and int(c) % 2 == 1])
even = sorted([c for c in s if c.isdigit() and int(c) % 2 == 0])

print(''.join(lower + upper + odd + even))