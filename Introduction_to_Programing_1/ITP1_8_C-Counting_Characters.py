## ITP1_8_C-Counting_Characters.py: Coded by Kinya MIURA, 240203
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_8_C

import sys
from collections import defaultdict

chars = defaultdict(int)
for line in sys.stdin:
    for char in line:
        if char.isalpha():
            chars[char.lower()] += 1

for i in range(26):
    cc = chr(ord('a') + i)
    print(f'{cc} : {chars[cc]}')

'''

'''

