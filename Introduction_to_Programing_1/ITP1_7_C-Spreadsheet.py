## ITP1_7_C-Spreadsheet.py: Coded by Kinya MIURA, 240203
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_C

r, c = map(int, input().split())
mm = [list(map(int, input().split())) for _ in range(r)]

ss = [0 for _ in range(c+1)]
for mmi in mm:
    mmi.append(sum(mmi))
    print(*mmi)
    for ii, mmii in enumerate(mmi):
        ss[ii] += mmii
print(*ss)


'''
r, c = map(int, input().split())
mm = [list(map(int, input().split())) for _ in range(r)]

ss = [0 for _ in range(c+1)]
for mmi in mm:
    for ii, mmii in enumerate(mmi):
        print(mmii, end=' ')
        ss[ii] += mmii
    ss[c] += sum(mmi)
    print(sum(mmi))
for ssi in ss[:c]:
    print(ssi, end=' ')
print(ss[c])
'''

