#Re.findall() & Re.finditer()
import re

s = input()

matches = re.findall(r'(?<=[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])([aeiouAEIOU]{2,})(?=[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])', s)

if matches:
    print(*matches, sep='\n')
else:
    print(-1)