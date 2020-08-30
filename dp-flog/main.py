# https://atcoder.jp/contests/abc176/tasks/abc176_d

n = int(input())
h = list(map(int, input().split()))

dp = []

for _ in range(n):
    dp.append(999999999)

dp[0] = 0

for i in range(len(dp)):
    dp[i] = min(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]))
    if i > 1:
        dp[i] = min(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]))

print(dp[n - 1])
