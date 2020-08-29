# https://atcoder.jp/contests/abc176/tasks/abc176_a

import math

n, x, t = list(map(int, input().split()))
print(math.ceil(n / x) * t)
