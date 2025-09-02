def best_bomb_spot(grid, m):
    n = len(grid)
    best_count = 0
    best_positions = []
    offset = m // 2

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            ci, cj = i + offset, j + offset
            if grid[ci][cj] != 1:
                continue

            count = 0
            destroyed = []
            for di in range(m):
                for dj in range(m):
                    r, c = i + di, j + dj
                    if grid[r][c] == 1:
                        count += 1
                        destroyed.append((r, c))

            if count > best_count:
                best_count = count
                best_positions = destroyed

    return best_count, best_positions


if __name__ == "__main__":
    # Read m (must be odd)
    m = int(input("Enter odd bomb size m (e.g., 3, 5, etc.): "))
    # Read grid size n
    n = int(input("Enter grid size n (n >= m): "))

    print(f"Enter the grid rows one by one (each row with {n} space-separated values, 0 or 1):")
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    max_destroyed, coords = best_bomb_spot(grid, m)

    print(f"\nMax islands destroyed: {max_destroyed}")
    print("Coordinates destroyed:", coords)
