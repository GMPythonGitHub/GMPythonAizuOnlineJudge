## ITP1_10_D-Distance_II.py: Coded by Kinya MIURA, 240206
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_D
## :: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_10_D

N = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

dd1, dd2, dd3, ddi = 0, 0, 0, 0
for Xi, Yi in zip(X, Y):
    dd1 += abs(Xi - Yi)
    dd2 += abs(Xi - Yi)**2
    dd3 += abs(Xi - Yi)**3
    ddi = max(ddi, abs(Xi - Yi))
dd2 = dd2**(1/2)
dd3 = dd3**(1/3)
print(dd1, dd2, dd3, ddi)


'''

'''

