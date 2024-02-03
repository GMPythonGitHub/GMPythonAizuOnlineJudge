## ITP1_7_D-Matrix_Multiplication.py: Coded by Kinya MIURA, 240203
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_D

n, m, l = map(int, input().split())

mma = [list(map(int, input().split())) for _ in range(n)]
mmb = [list(map(int, input().split())) for _ in range(m)]

for ni in range(n):
    for li in range(l):
        cc = 0
        for mi in range(m):
            cc += mma[ni][mi] * mmb[mi][li]
        if li < l-1:
            print(cc, end=' ')
        else:
            print(cc)


'''

'''

