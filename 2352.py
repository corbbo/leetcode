# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

def equalPairs(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i] == grid[j]:
                count += 1
    return count