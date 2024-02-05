## ITP1_9_B-Shuffle.py: Coded by Kinya MIURA, 240205
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_9_B
## :: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_9_B

while True:
    S = input()
    if S == '-':
        break
    lls = len(S)
    SS = S + S

    M = int(input())
    pos = 0
    for _ in range(M):
        pos += int(input())
    pos = pos % lls
    print(SS[pos:pos+lls])


'''

'''

