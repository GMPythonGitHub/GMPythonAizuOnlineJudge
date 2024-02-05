## ITP1_2_D-Circle_in_a_Rectangle.py: Coded by Kinya MIURA, 240119
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_2_D
## :: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_2_D

W, H, xx, yy, rr = list(map(int, input().split()))

if rr <= xx <= W - rr and rr <= yy <= H - rr:
    print('Yes')
else:
    print('No')


'''

'''

