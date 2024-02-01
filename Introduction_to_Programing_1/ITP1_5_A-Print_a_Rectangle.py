## ITP1_5_A-Print_a_Rectangle.py: Coded by Kinya MIURA, 240130
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_5_A

while True:
    H, W = map(int, input().split())
    if H == W == 0:
        break
    for _ in range(H):
        print('#'*W)
    print()


'''

'''

