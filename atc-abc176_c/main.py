# https://atcoder.jp/contests/abc176/tasks/abc176_c

n = int(input())
s = list(map(int, input().split()))

rate = 0
count = 0
for i, v in enumerate(s):
    if i == 0:
        rate = v
        continue

    if rate > v:
        tmp = rate - v
        count += tmp
    else:
        rate = v

print(count)
