## ITP1_5_C-Print_a_Chessboard.py: Coded by Kinya MIURA, 240130
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_5_C
## :: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_5_C

while True:
    H, W = map(int, input().split())
    if H == W == 0:
        break
    for hh in range(H):
        if hh % 2 == 0:
            print('#.' * (W // 2) + '#' * (W % 2))
        else:
            print('.#' * (W // 2) + '.' * (W % 2))
    print()


'''

'''

