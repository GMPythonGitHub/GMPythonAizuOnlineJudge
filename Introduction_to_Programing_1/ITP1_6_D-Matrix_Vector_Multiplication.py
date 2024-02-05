## ITP1_6_D-Matrix_Vector_Multiplication.py: Coded by Kinya MIURA, 240203
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_6_D
## :: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_6_D

n, m = map(int, input().split())

mm = [map(int, input().split()) for _ in range(n)]
vv = [int(input()) for _ in range(m)]

for mmi in mm:
    ss = 0
    for mmii, vvi in zip(mmi, vv):
        ss += mmii * vvi
    print(ss)


'''

'''

