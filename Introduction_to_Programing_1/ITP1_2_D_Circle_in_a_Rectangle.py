## ITP1_2_D_Circle_in_a_Rectangle.py: Coded by Kinya MIURA, 240119

W, H, xx, yy, rr = list(map(int, input().split()))

if rr <= xx <= W - rr and rr <= yy <= H - rr:
    print('Yes')
else:
    print('No')


'''

'''

