## ITP1_3_C-Swapping_Two_Numbers.py: Coded by Kinya MIURA, 240130
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_C

while True:
    xx, yy = map(int, input().split())
    if xx == yy == 0:
        break
    else:
        if xx <= yy:
            print(xx, yy)
        else:
            print(yy, xx)

'''

'''

