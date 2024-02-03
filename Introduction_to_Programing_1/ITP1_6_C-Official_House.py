## ITP1_6_C-Official_House.py: Coded by Kinya MIURA, 240203
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_6_D

n, = map(int, input().split())

residents = [ [ [0 for _ in range(10)] for _ in range(3)] for _ in range(4) ]
for _ in range(n):
    b, f, r, v = map(int, input().split())
    residents[b-1][f-1][r-1] += v
# print(f'{residents = }')

for bbi in range(4):
    for ffi in range(3):
        for rri in range(10):
            print(f'{residents[bbi][ffi][rri]:2d}', end='')
        print()
    if bbi < 4-1:
        print('#'*20)


'''

'''

