# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

def equalPairs(grid): # wrong!
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i] == grid[j]:
                count += 1
    return count

if __name__ == "__main__":
    print(equalPairs([[0,0,0],[0,1,0],[0,0,0]])) # 12
    print(equalPairs([[1,0,0],[0,0,0],[0,0,0]])) # 8
    print(equalPairs([[1,1,1],[1,1,1],[1,1,1]])) # 27
    print(equalPairs([[1,0,0],[0,1,0],[0,0,1]])) # 6
    print(equalPairs([[0,1,1],[1,0,1],[1,1,0]])) # 6
    print(equalPairs([[0,1,1],[1,1,1],[1,1,0]])) # 9
    print(equalPairs([[0,1,1],[1,1,1],[1,1,1]])) # 12
    print(equalPairs([[0,0,0],[0,0,0],[0,0,0]])) # 27
    print(equalPairs([[1,0,0],[0,1,0],[0,0,0]])) # 8
    print(equalPairs([[1,1,1],[1,1,1],[1,1,1]])) # 27
    print(equalPairs([[1,0,0],[0,0,0],[0,0,0]])) # 8