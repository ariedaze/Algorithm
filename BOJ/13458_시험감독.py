N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0

for idx in range(N):
    A[idx] -= B
    result += 1
    if A[idx] > 0:
        result += A[idx] // C
        if A[idx] % C:
            result += 1


print(result)
