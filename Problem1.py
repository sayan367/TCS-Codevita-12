from collections import deque

def min_moves_to_destination(M, N, grid, source, destination, move_rule):
    # Directions based on the move rule (dx, dy)
    dx, dy = move_rule
    
    # All possible movements based on the move rules
    directions = [
        (dx, dy),         # Forward
        (dy, -dx),       # Right (90 degree clockwise)
        (-dy, dx),       # Left (90 degree anticlockwise)
        (-dx, -dy)       # Backward (180 degrees)
    ]
    
    # BFS setup
    queue = deque([(source[0], source[1], 0)])  # (x, y, moves)
    visited = set()
    visited.add((source[0], source[1]))

    while queue:
        x, y, moves = queue.popleft()
        
        # Check if we reached the destination
        if (x, y) == (destination[0], destination[1]):
            return moves
        
        # Explore all possible directions
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            # Check if the new position is within bounds and valid
            if 0 <= new_x < M and 0 <= new_y < N and grid[new_x][new_y] == 0:
                if (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y, moves + 1))
    
    return -1  # If destination is unreachable

# Input reading
M, N = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(M)]
source = tuple(map(int, input().strip().split()))
destination = tuple(map(int, input().strip().split()))
move_rule = tuple(map(int, input().strip().split()))

# Finding the minimum moves
result = min_moves_to_destination(M, N, grid, source, destination, move_rule)
print(result)
