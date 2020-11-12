N = int(input())
dp = [0] * 20 # 15 + 5

for i in range(N):
    t, p = map(int, input().split())
    if dp[i] > dp[i+1]:
        dp[i+1] = dp[i]
    if dp[i + t] < dp[i] + p:
        dp[i+t] = dp[i] + p
    # print(t, p, dp)
print(dp[N])