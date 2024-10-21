from collections import deque

def bfs_min_moves(grid, start, end, move_rule):
    M, N = len(grid), len(grid[0])
    directions = [
        (1, 0),  # Forward
        (0, 1),  # Right
        (-1, 0), # Left
        (0, -1)  # Backward
    ]
    
    print(f"Debug: Grid size: {M}x{N}, Start: {start}, End: {end}, Move rule: {move_rule}")
    
    # Boundary and validity checks
    if not (0 <= start[0] < M and 0 <= start[1] < N and grid[start[0]][start[1]] == 0):
        print("Debug: Invalid start position")
        return -1
    if not (0 <= end[0] < M and 0 <= end[1] < N and grid[end[0]][end[1]] == 0):
        print("Debug: Invalid end position")
        return -1
    
    # BFS queue
    queue = deque([(start[0], start[1], 0)])  # (x, y, moves)
    visited = set()
    visited.add(start)
    
    while queue:
        x, y, moves = queue.popleft()
        print(f"Debug: Current position: ({x}, {y}), Moves: {moves}")
        
        # Check if we've reached the destination
        if (x, y) == end:
            return moves
        
        # Explore all four directions
        for i, (dx, dy) in enumerate(directions):
            # Calculate the next position based on the move rule
            next_x = x + dx * move_rule[0] + dy * move_rule[1]
            next_y = y + dy * move_rule[0] - dx * move_rule[1]
            print(f"Debug: Direction {i}, Next position: ({next_x}, {next_y})")
            
            # Check if the next position is within bounds and not visited
            if 0 <= next_x < M and 0 <= next_y < N and grid[next_x][next_y] == 0:
                if (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y, moves + 1))
            else:
                print(f"Debug: Invalid or visited position: ({next_x}, {next_y})")
    
    return -1  # If there's no path to the destination

# Read input
M, N = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(M)]
source = tuple(map(int, input().strip().split()))
destination = tuple(map(int, input().strip().split()))
move_rule = tuple(map(int, input().strip().split()))

print("Debug: Input read successfully")
print(f"Debug: Grid: {grid}")
print(f"Debug: Source: {source}")
print(f"Debug: Destination: {destination}")
print(f"Debug: Move rule: {move_rule}")

# Get the minimum moves
result = bfs_min_moves(grid, source, destination, move_rule)
print(f"Result: {result}")