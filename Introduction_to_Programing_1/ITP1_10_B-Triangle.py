## ITP1_10_B-Triangle.py: Coded by Kinya MIURA, 240206
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_B
## :: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_10_B

import math

aa, bb, C = map(float, input().split())

S = aa * bb * math.sin(math.radians(C)) / 2
cc = math.sqrt(aa**2 + bb**2 - 2*aa*bb*math.cos(math.radians(C)))
hh = 2 * S / aa

print(S, aa+bb+cc, hh)


'''

'''

