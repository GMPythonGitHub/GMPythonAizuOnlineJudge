## ITP1_9_A-Finding_a_Word.py: Coded by Kinya MIURA, 240205
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_9_A
## :: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_9_A

W = input()
count = 0
while True:
    S = input()
    if S == 'END_OF_TEXT':
        break
    SS = list(S.lower().split())
    # print(SS)
    for SSi in SS:
        if SSi == W:
            count += 1
    # print('a', count)
print(count)


'''
W = input()
W = ' ' + W + ' '
llw = len(W)
count = 0
while True:
    S = input()
    if S == 'END_OF_TEXT':
        break
    T = ' ' + S.lower() + ' '
    # print(T)
    llt = len(T)
    for ii in range(llt-llw+1):
        if T[ii:ii+llw] == W:
            count += 1
    # print('a', count)
print(count)
'''

