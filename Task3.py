def max_damage_coords(grid, m):
    n = len(grid); r = m // 2

    # build 2-D prefix sum
    ps = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        row_sum = 0
        for j in range(n):
            row_sum += grid[i][j]
            ps[i+1][j+1] = ps[i][j+1] + row_sum

    def rect_sum(r1,c1,r2,c2):  # inclusive
        return (ps[r2+1][c2+1] - ps[r1][c2+1]
                - ps[r2+1][c1] + ps[r1][c1])

    best = -1
    best_centers = []
    for i in range(r, n-r):
        for j in range(r, n-r):
            if grid[i][j] == 0:   # center is water → dud
                continue
            s = rect_sum(i-r, j-r, i+r, j+r)
            if s > best:
                best, best_centers = s, [(i, j)]
            elif s == best:
                best_centers.append((i, j))

    # convert to requested coordinates
    results = []
    for (i,j) in best_centers:
        x, y = j, n-1-i
        results.append((x, y))
    return best, results
