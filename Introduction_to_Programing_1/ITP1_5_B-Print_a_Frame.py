## ITP1_5_B-Print_a_Frame.py: Coded by Kinya MIURA, 240130
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_5_B

while True:
    H, W = map(int, input().split())
    if H == W == 0:
        break
    print('#' * W)
    for _ in range(H-2):
        print('#'+'.'*(W-2)+'#')
    print('#' * W)
    print()


'''

'''

