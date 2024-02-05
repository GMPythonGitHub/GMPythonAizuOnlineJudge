## ITP1_6_A-Reversing_Numbers.py: Coded by Kinya MIURA, 240203
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_6_A
## :: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_6_A

n, = map(int, input().split())
a =  list(input().split())

print(*reversed(a))


'''
n, = map(int, input().split())
a =  list(input().split())

for ii, ai in enumerate(reversed(a)):
    if ii == 0:
       print(ai, end='')
    else:
       print(' '+ai, end='')
print()
'''

