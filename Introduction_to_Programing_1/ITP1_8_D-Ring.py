## ITP1_8_C-Counting_Characters.py: Coded by Kinya MIURA, 240203
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_8_D
## :: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_8_D

S = input()
T = input()
lls, llt = len(S), len(T)
SS = S + S

for ii in range(lls):
    if T == SS[ii:ii+llt]:
        exit(print('Yes'))
print('No')




'''

'''

