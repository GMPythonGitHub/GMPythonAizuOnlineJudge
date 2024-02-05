## ITP1_4_C-Simple_Calculator.py: Coded by Kinya MIURA, 240130
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_4_C
## :: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_4_C

while True:
    ss = input()
    pp = ss.index(' ')
    aa = int(ss[:pp])
    op = ss[pp+1:pp+2]
    bb = int(ss[pp+3:])
    if op == '?':
        break
    if op == '+':
        print(aa + bb)
    elif op == '-':
        print(aa - bb)
    elif op == '*':
        print(aa * bb)
    elif op == '/':
        print(aa // bb)


'''

'''

