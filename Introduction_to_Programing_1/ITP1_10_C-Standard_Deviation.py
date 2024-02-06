## ITP1_10_C-Standard_Deviation.py: Coded by Kinya MIURA, 240206
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_C
## :: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_10_C

import math

while True:
    N = int(input())
    if N == 0:
        break
    S = list(map(int, input().split()))

    mm = sum(S) / N
    # print(mm, S)
    vv = 0
    for Si in S:
        vv += (Si-mm)**2
    aa = math.sqrt(vv/N)
    print(aa)


'''

'''

