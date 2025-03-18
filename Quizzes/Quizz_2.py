# Given a map of squares disposed in a rectangular grid find the shortest path, in number of moves, from a start point S to an end point E.

# There is a rule to be respected: a sequence of three moves will be repeated until the end point is reached. The first move should pass through one square, in the second through two squares and in the third through three squares. In each move, you must pass through the corresponding number of squares, without changing your direction during a move. You must begin with 1 square and repeat the sequence of 1, 2 and 3 squares until the end is reached. The end can be reached at the end of any of these moves. 

# maze eg

# Define function solve that receives a file name with the maze information in the following format:

# File. The first line of the file contains two integers separated by a single space: L (2<= L<= 300) corresponding to the number of rows and C (2 <= C<= 300) corresponding to the number of columns.

# Each of the following L lines contains C characters. For each character, a dot  "."  represents a square, a hash mark "#" represents a wall, and the capital letters "S" and "E"  represent the start and the end position respectively.

# The function outputs the number of moves from "S" to "E" or the string "NO" if there is no solution.

# print(solve('input1.txt')) -> 27

# print(solve('input2.txt')) -> 48

# print(solve('input3.txt')) -> NO

from collections import deque

def solve(file_name):
    maze = []
    start_position = None
    end_position = None
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    with open(file_name) as f:  # read the file and get the maze information
        rows, cols = map(int, f.readline().split())
        for i in range(rows):
            line = f.readline().strip()
            maze.append(line)
            if 'S' in line:
                start_position = (i, line.index('S'))
            if 'E' in line:
                end_position = (i, line.index('E'))
    if not start_position or not end_position:  # check if the start and end positions are valid
        return 'NO'
    
    def bfs(end_position, frontier):
        visited = set()
        while frontier:
            (row, col), moves, step_size = frontier.popleft()
            if (row, col, step_size) in visited:
                continue
            visited.add((row, col, step_size))
            if (row, col) == end_position:
                return moves
            for dr, dc in directions:
                r, c = row, col
                r += dr * step_size
                c += dc * step_size
                if r < 0 or r >= len(maze) or c < 0 or c >= len(maze[0]) or maze[r][c] == '#':
                    continue
                if (r, c) == end_position:
                    return moves + 1
                if (r, c, step_size % 3 + 1) not in visited:
                    frontier.append(((r, c), moves + 1, step_size % 3 + 1))
        return 'NO'
    
    frontier = deque([(start_position, 0, 1)])  # initialize frontier with start position, move count, and step size
    return bfs(end_position, frontier)

print(solve('./input1.txt'))  # Example usage