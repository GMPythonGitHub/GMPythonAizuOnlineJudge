## ITP1_1_D-Watch.py: Coded by Kinya MIURA, 240119
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_D

ss,  = map(int, input().split())

mm = ss // 60
hh = mm // 60
print(str(hh)+':'+str(mm%60)+':'+str(ss%60))


'''

'''

