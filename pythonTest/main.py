def route_finding(N, K):
    MOD = 10**9 + 7
    pvar = [[[0 for _ in range(K+1)] for _ in range(N+1)] for _ in range(N+1)]

    pvar[0][0][K] = 1

    for x in range(N):
        for y in range(N+1):
            for i in range(K+1):
                if y < N and i > 0:
                    pvar[x+1][y+1][i-1] = (pvar[x+1][y+1][i-1] + pvar[x][y][i]) % MOD

                n_y = max(0, y-1)
                n_k = K if n_y == 0 else i
                pvar[x+1][n_y][n_k] = (pvar[x+1][n_y][n_k] + pvar[x][y][i]) % MOD

    return pvar[N][0][K] % MOD

N, K = map(int, input().split())
print(route_finding(N, K))