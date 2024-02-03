## ITP1_6_B-Finding_Missing_Cards.py: Coded by Kinya MIURA, 240203
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_6_B

from collections import defaultdict

n, = map(int, input().split())

cards = defaultdict(list)
for _ in range(n):
    st, num = input().split()
    cards[st].append(int(num))
# print(f'{cards = }')

for sti in ['S', 'H', 'C', 'D']:
    nums = cards[sti]
    for ii in range(1, 13+1):
        if ii not in nums:
            print(sti, ii)



'''

'''

