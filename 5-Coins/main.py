c500 = int(input())
c100 = int(input())
c50 = int(input())
r = int(input())

cnt = 0

for i500 in range(c500 + 1):
    r1 = r - 500 * i500
    for i100 in range(c100 + 1):
        r2 = r1 - 100 * i100
        if 0 <= r2 <= c50 * 50:
            cnt += 1
print(cnt)
