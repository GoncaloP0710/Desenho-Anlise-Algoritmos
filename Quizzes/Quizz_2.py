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
