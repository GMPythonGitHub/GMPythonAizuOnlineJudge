## ITP1_8_A-Toggling_Cases.py: Coded by Kinya MIURA, 240203
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_8_A

x = input()

y = ''
for xi in x:
    if ord('A') <= ord(xi) <= ord('Z'):
        y += chr(ord(xi) + ord('a') - ord('A'))
    elif ord('a') <= ord(xi) <= ord('z'):
        y += chr(ord(xi) + ord('A') - ord('a'))
    else:
        y += xi
print(T)


'''

'''

