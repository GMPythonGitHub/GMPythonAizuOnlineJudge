## ITP1_8_B-Sum_of_Numbers.py: Coded by Kinya MIURA, 240203
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_8_B
## :: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_8_B

while True:
    x = input()
    if x == '0':
        break
    y = str(x)
    ss = 0
    for yi in y:
        ss += int(yi)
    print(ss)


'''

'''

