## ITP1_9_D-Transformation.py: Coded by Kinya MIURA, 240205
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_9_D
## :: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_9_D

S = input()

Q = int(input())
for _ in range(Q):
    T = input()
    # print(T)
    if T[:len('print')] == 'print':
        # print(T)
        _, aa, bb = T.split()
        aa, bb = int(aa), int(bb)
        print(S[aa:bb+1])
    elif T[:len('reverse')] == 'reverse':
        # print(T)
        _, aa, bb = T.split()
        aa, bb = int(aa), int(bb)
        S = S[:aa] + ''.join(list(reversed(list(S[aa:bb+1])))) + S[bb+1:]
    elif T[:len('replace')] == 'replace':
        # print(T)
        _, aa, bb, pp = T.split()
        aa, bb = int(aa), int(bb)
        S = S[:aa] + pp + S[bb+1:]




'''

'''

