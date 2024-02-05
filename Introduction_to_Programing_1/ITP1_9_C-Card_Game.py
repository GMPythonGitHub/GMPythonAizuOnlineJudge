## ITP1_9_C-Card_Game.py: Coded by Kinya MIURA, 240205
## ::https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_9_C
## :: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_9_C

N = int(input())
count_A, count_B = 0, 0
for _ in range(N):
    A, B = input().split()
    if A > B:
        count_A += 3
    elif B > A:
        count_B += 3
    else:
        count_A += 1
        count_B += 1
print(count_A, count_B)


'''

'''

