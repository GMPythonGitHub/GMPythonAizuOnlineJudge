## ITP1_4_D-Min,_Max_and_Sum.py: Coded by Kinya MIURA, 240130
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_4_D
## :: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_4_D

N, = map(int, input().split())
A = list(map(int, input().split()))

print(min(A), max(A), sum(A))


'''
nmin = +10**7
nmax = -10**7
nsum = 0

for Ai in A:
    if Ai < nmin:
        nmin = Ai
    if Ai > nmax:
        nmax = Ai
    nsum += Ai
print(nmin, nmax, nsum)
'''

