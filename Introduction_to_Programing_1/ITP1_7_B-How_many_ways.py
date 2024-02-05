## ITP1_7_B-How_many_ways.py: Coded by Kinya MIURA, 240203
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B
## :: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_7_B

while True:
    n, x = map(int, input().split())
    if n == x == 0:
        break
    if n > n *3 - 3:
        print(0)
    else:
        cont = 0
        for aa in range(1, n-1):
            if aa > x - (2 * aa + 3):
                continue
            for bb in range(aa+1, n):
                cc = x - aa - bb
                if bb < cc <= n:
                    cont += 1
        print(cont)


'''

'''

