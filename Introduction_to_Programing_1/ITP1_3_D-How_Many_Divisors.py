## ITP1_3_D-How_Many_Divisors.py: Coded by Kinya MIURA, 240130
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_D

aa, bb, cc = map(int, input().split())

cont = 0
for xx in range(aa, bb+1):
    if cc % xx == 0:
        cont += 1
print(cont)

'''

'''

